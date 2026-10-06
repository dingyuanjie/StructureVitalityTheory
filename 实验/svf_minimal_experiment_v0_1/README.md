# SVF Minimal Experiment v0.1

这是“结构生力科学版”的第一个最小、可证伪玩具实验。

## 它测试什么

候选假说：

\[
\Lambda = \frac{RMC}{D}
\]

可能是一个跨参数条件的控制量，其中：

- `R`：反馈/结构可塑性增益
- `M`：记忆痕迹保持
- `C`：有效耦合密度
- `D`：耗散与噪声

系统的可观测“结构生力”暂定义为：

\[
V = G \times P_\tau
\]

其中：

- `G`：训练后新形成的、与重复输入结构一致的连接结构增量
- `P_tau`：撤去输入并延迟后，系统状态对过去输入仍保留的信息量（归一化互信息）

关键点：**Lambda 没有直接写进动力学。**
R、M、C、D 是分别进入模拟器的，最后才计算 Lambda 并检查是否出现数据坍缩或“结构生成带”。

## 最小动力学

状态：

\[
x_{t+1}=\tanh[(1-D)x_t + W_t x_t + u_t + \epsilon(D)]
\]

记忆痕迹：

\[
h_{t+1}=Mh_t+(1-M)x_{t+1}
\]

结构更新（adaptive 条件）：

\[
W_{t+1}=W_t+\eta R\cdot F(h_t)-\eta D\cdot W_t
\]

连接掩码密度由 `C` 独立控制。

## 三种条件

1. `adaptive`：正常反馈塑形结构。
2. `frozen`：结构冻结，不允许学习。
3. `shuffled`：更新强度保留，但把反馈与原结构的对应关系打乱。

后两者是负对照。

## 运行

```bash
pip install -r requirements.txt
python svf_minimal_experiment.py --outdir results
```

更快的 smoke test：

```bash
python svf_minimal_experiment.py --configs 40 --seeds 1 --controls 8 --episodes 60
```

更稳的版本：

```bash
python svf_minimal_experiment.py --configs 500 --seeds 5 --controls 60 --episodes 200 --delay-steps 12
```

## 输出

- `sweep_results.csv`
- `control_results.csv`
- `lambda_binned_summary.csv`
- `fit_summary.json`
- `phase_curve.png`

## 这不是“证明”

即使这个玩具系统出现漂亮的倒 U 曲线，也只能说明：
在**这个特定机制模型**里，候选控制量值得继续研究。

真正支持“跨系统结构规律”，至少还需要把同一预注册指标拿去测试：

1. 不同人工动力系统；
2. RNN / Transformer memory；
3. 群体智能或人工生命；
4. 神经科学数据；
5. 最后才谈更广泛的自然系统。

