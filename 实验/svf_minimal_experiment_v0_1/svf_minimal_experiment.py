#!/usr/bin/env python3
"""
SVF Minimal Experiment v0.1
A toy falsifiable test of the hypothesis that adaptive structural organization
depends on feedback (R), memory (M), coupling (C), and dissipation (D), with
Lambda = R*M*C/D as a candidate cross-condition control variable.

Important:
- This is a toy model, not evidence for a universal law by itself.
- Lambda is NOT injected directly into the dynamics.
- R, M, C, D enter the simulator independently.
"""

from __future__ import annotations
import argparse
import math
from dataclasses import dataclass, asdict
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


@dataclass
class SimConfig:
    n_nodes: int = 32
    n_patterns: int = 4
    episodes: int = 100
    stim_steps: int = 3
    delay_steps: int = 8
    probe_repeats: int = 10
    eta: float = 0.03
    recurrent_gain: float = 1.1


def normalized_mutual_information(y_true, y_pred, k):
    cm = np.zeros((k, k), dtype=float)
    for a, b in zip(y_true, y_pred):
        cm[int(a), int(b)] += 1.0
    if cm.sum() == 0:
        return 0.0
    p = cm / cm.sum()
    pa = p.sum(axis=1, keepdims=True)
    pb = p.sum(axis=0, keepdims=True)
    mi = 0.0
    for i in range(k):
        for j in range(k):
            if p[i, j] > 0 and pa[i, 0] > 0 and pb[0, j] > 0:
                mi += p[i, j] * math.log(
                    p[i, j] / (pa[i, 0] * pb[0, j]) + 1e-15
                )
    return float(mi / math.log(k))


def run_condition(R, M, C, D, seed, cfg=None, control="adaptive"):
    """
    R: feedback/plasticity gain, positive dimensionless
    M: trace retention in [0, 1)
    C: connection probability in (0, 1]
    D: dissipation/noise level, positive
    control: adaptive | frozen | shuffled
    """
    cfg = cfg or SimConfig()
    rng = np.random.default_rng(seed)

    N, K = cfg.n_nodes, cfg.n_patterns
    groups = np.repeat(np.arange(K), math.ceil(N / K))[:N]

    # Structural coupling mask. C independently controls graph density.
    A = (rng.random((N, N)) < C).astype(float)
    A = np.triu(A, 1)
    A = A + A.T

    # Small random initial structure.
    W = rng.normal(0, 0.04, size=(N, N)) * A
    W = (W + W.T) / 2.0
    np.fill_diagonal(W, 0.0)
    W0 = W.copy()

    x = np.zeros(N)
    h = np.zeros(N)
    scale = max(1.0, math.sqrt(max(C * N, 1e-9)))

    def step(x, h, W, u, learn=True):
        rec = cfg.recurrent_gain * (W @ x) / scale

        # D independently increases perturbation and erodes state retention.
        noise = rng.normal(0, 0.02 + 0.12 * D, size=N)
        x_new = np.tanh((1.0 - min(D, 0.95)) * x + rec + u + noise)

        # M independently controls the persistence of an activity trace.
        h_new = M * h + (1.0 - M) * x_new

        if learn and control != "frozen":
            centered = h_new - h_new.mean()
            dW = np.outer(centered, centered) / N

            # Shuffled control preserves update magnitude but destroys
            # the structure-to-feedback alignment.
            if control == "shuffled":
                perm = rng.permutation(N)
                dW = dW[perm][:, perm]

            # R independently scales feedback-driven structural plasticity.
            W_new = W + cfg.eta * R * dW * A - cfg.eta * D * 0.12 * W
            W_new = (W_new + W_new.T) / 2.0
            np.fill_diagonal(W_new, 0.0)
            W_new = np.clip(W_new, -1.5, 1.5)
        else:
            W_new = W

        return x_new, h_new, W_new

    # TRAINING: recurrent patterned experience with blank-delay periods.
    for _ in range(cfg.episodes):
        p = int(rng.integers(K))
        for _ in range(cfg.stim_steps):
            u = np.where(groups == p, 0.9, -0.18)
            x, h, W = step(x, h, W, u, learn=True)
        for _ in range(cfg.delay_steps):
            x, h, W = step(x, h, W, np.zeros(N), learn=True)

    # STRUCTURE GROWTH:
    # The recurring inputs define K latent communities. A useful newly formed
    # structure should preferentially strengthen within-pattern relations.
    same = (groups[:, None] == groups[None, :]) & (A > 0)
    diff = (groups[:, None] != groups[None, :]) & (A > 0)

    def contrast(W_):
        if same.sum() == 0 or diff.sum() == 0:
            return 0.0
        return float(np.mean(np.abs(W_[same])) - np.mean(np.abs(W_[diff])))

    q0 = contrast(W0)
    q1 = contrast(W)
    G = max(0.0, q1 - q0)

    # PROBE:
    # Freeze structure. Present each pattern, remove input, then ask whether
    # the delayed state still contains decodable information about the pattern.
    X, y = [], []
    for p in range(K):
        for _ in range(cfg.probe_repeats):
            xp = np.zeros(N)
            hp = np.zeros(N)
            Wp = W
            for _ in range(cfg.stim_steps):
                u = np.where(groups == p, 0.9, -0.18)
                xp, hp, Wp = step(xp, hp, Wp, u, learn=False)
            for _ in range(cfg.delay_steps):
                xp, hp, Wp = step(xp, hp, Wp, np.zeros(N), learn=False)
            X.append(xp)
            y.append(p)

    X = np.asarray(X)
    y = np.asarray(y)

    train_idx = np.array(
        [(r % 2 == 0) for _p in range(K) for r in range(cfg.probe_repeats)]
    )
    test_idx = ~train_idx

    centroids = np.array([X[train_idx & (y == k)].mean(axis=0) for k in range(K)])
    Xt, yt = X[test_idx], y[test_idx]
    dist = ((Xt[:, None, :] - centroids[None, :, :]) ** 2).mean(axis=2)
    yp = dist.argmin(axis=1)

    accuracy = float((yp == yt).mean())
    P_tau = normalized_mutual_information(yt, yp, K)

    # Observable structural vitality:
    # must BOTH create pattern-aligned structure and retain delayed information.
    V = G * P_tau

    return {
        "R": float(R),
        "M": float(M),
        "C": float(C),
        "D": float(D),
        "Lambda": float(R * M * C / max(D, 1e-12)),
        "P_tau": float(P_tau),
        "accuracy": accuracy,
        "G_structure": float(G),
        "V": float(V),
        "Q_before": float(q0),
        "Q_after": float(q1),
        "control": control,
        "seed": int(seed),
    }


def sample_parameters(rng):
    # Broad ranges deliberately include weak, productive, and destabilizing regimes.
    R = 10 ** rng.uniform(math.log10(0.05), math.log10(8.0))
    M = rng.uniform(0.10, 0.95)
    C = rng.uniform(0.10, 0.95)
    D = 10 ** rng.uniform(math.log10(0.05), math.log10(0.80))
    return R, M, C, D


def run_sweep(n_configs=160, seeds=2, base_seed=313, cfg=None):
    cfg = cfg or SimConfig()
    rng = np.random.default_rng(base_seed)
    rows = []

    params = [sample_parameters(rng) for _ in range(n_configs)]
    for i, (R, M, C, D) in enumerate(params):
        for s in range(seeds):
            rows.append(
                run_condition(
                    R, M, C, D,
                    seed=base_seed + i * 17 + s,
                    cfg=cfg,
                    control="adaptive",
                )
            )

    return pd.DataFrame(rows), params


def run_controls(params, n=24, seed=313, cfg=None):
    cfg = cfg or SimConfig()
    rows = []
    for i, (R, M, C, D) in enumerate(params[:n]):
        for control in ("adaptive", "frozen", "shuffled"):
            rows.append(
                run_condition(
                    R, M, C, D,
                    seed=seed + i * 23,
                    cfg=cfg,
                    control=control,
                )
            )
    return pd.DataFrame(rows)


def analyze(df, outdir):
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    d = df.copy()
    d["log10_Lambda"] = np.log10(d["Lambda"].clip(lower=1e-12))
    d["lambda_bin"] = pd.qcut(d["log10_Lambda"], 8, duplicates="drop")

    agg = (
        d.groupby("lambda_bin", observed=True)
        .agg(
            Lambda_median=("Lambda", "median"),
            V_mean=("V", "mean"),
            V_sem=("V", lambda x: x.std(ddof=1) / math.sqrt(max(len(x), 1))),
            P_mean=("P_tau", "mean"),
            G_mean=("G_structure", "mean"),
            accuracy_mean=("accuracy", "mean"),
            n=("V", "size"),
        )
        .reset_index(drop=True)
    )
    agg.to_csv(outdir / "lambda_binned_summary.csv", index=False)

    x = d["log10_Lambda"].to_numpy()
    y = d["V"].to_numpy()
    coef = np.polyfit(x, y, 2)
    pred = np.polyval(coef, x)
    sst = np.sum((y - y.mean()) ** 2)
    r2 = 1.0 - np.sum((y - pred) ** 2) / sst if sst > 0 else 0.0
    peak_log = -coef[1] / (2 * coef[0]) if coef[0] != 0 else np.nan
    peak_lambda = 10 ** peak_log if np.isfinite(peak_log) else np.nan

    summary = {
        "quadratic_a": float(coef[0]),
        "quadratic_b": float(coef[1]),
        "quadratic_c": float(coef[2]),
        "quadratic_r2": float(r2),
        "candidate_peak_lambda": float(peak_lambda),
        "n_rows": int(len(d)),
    }

    with open(outdir / "fit_summary.json", "w", encoding="utf-8") as f:
        import json
        json.dump(summary, f, indent=2, ensure_ascii=False)

    plt.figure(figsize=(8, 5))
    plt.errorbar(
        agg["Lambda_median"],
        agg["V_mean"],
        yerr=agg["V_sem"],
        marker="o",
        capsize=3,
    )
    plt.xscale("log")
    plt.xlabel("Candidate control variable Λ = R·M·C / D")
    plt.ylabel("Observed structural vitality V = G × Pτ")
    plt.title("SVF Minimal Experiment v0.1 — binned phase curve")
    plt.tight_layout()
    plt.savefig(outdir / "phase_curve.png", dpi=180)
    plt.close()

    return agg, summary


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--outdir", default="svf_results")
    parser.add_argument("--configs", type=int, default=160)
    parser.add_argument("--seeds", type=int, default=2)
    parser.add_argument("--base-seed", type=int, default=313)
    parser.add_argument("--controls", type=int, default=24)
    parser.add_argument("--episodes", type=int, default=100)
    parser.add_argument("--delay-steps", type=int, default=8)
    args = parser.parse_args()

    cfg = SimConfig(episodes=args.episodes, delay_steps=args.delay_steps)
    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    df, params = run_sweep(
        n_configs=args.configs,
        seeds=args.seeds,
        base_seed=args.base_seed,
        cfg=cfg,
    )
    df.to_csv(out / "sweep_results.csv", index=False)

    controls = run_controls(
        params,
        n=min(args.controls, len(params)),
        seed=args.base_seed,
        cfg=cfg,
    )
    controls.to_csv(out / "control_results.csv", index=False)

    agg, summary = analyze(df, out)

    print("Finished.")
    print(f"Rows: {len(df)}")
    print(f"Candidate peak Lambda: {summary['candidate_peak_lambda']:.4g}")
    print(f"Quadratic R^2: {summary['quadratic_r2']:.3f}")
    print(f"Results: {out.resolve()}")


if __name__ == "__main__":
    main()
