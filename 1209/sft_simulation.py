import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button

# ======================
# 结构生力理论 - 可交互优化版
# ======================

np.random.seed(42)

# 基础参数
dt = 0.01
total_steps = 500
levels = ['细胞', '人', '社会', '文明', '地球']
N_level = len(levels)

# 可调参数（初始值）
init_k = 0.6       # 耦合强度
init_D = 0.02      # 耗散系数
init_S_c = 1.0     # 进化阈值
init_S_c2 = 2.0    # 崩溃阈值

# 初始化数组
t = np.arange(total_steps) * dt

def simulate(k, D, S_c, S_c2):
    S = np.zeros((N_level, total_steps))
    I = np.zeros((N_level, total_steps))
    E = np.zeros((N_level, total_steps))

    # 初始状态
    for n in range(N_level):
        S[n, 0] = 1.0
        I[n, 0] = 1.0

    for i in range(1, total_steps):
        # 顶层外扰（地球）
        E[-1, i] = 1.5 + 0.2*np.sin(0.05*i) + 0.1*np.random.randn()
        # 下层外扰 = 上层结构 + 噪声
        for n in range(N_level-2, -1, -1):
            E[n, i] = S[n+1, i-1] + 0.05*np.random.randn()

        # 更新每一层
        for n in range(N_level):
            I[n, i] = I[n, i-1] + 0.01 * S[n, i-1]
            dS = k * (E[n, i] - I[n, i]) * dt - D * S[n, i-1] * dt
            S[n, i] = S[n, i-1] + dS
            S[n, i] = max(S[n, i], 0.0)  # 防止负数

    return S, I, E

# 初始仿真
S, I, E = simulate(init_k, init_D, init_S_c, init_S_c2)

# ======================
# 绘图 + 交互控件
# ======================
fig = plt.figure(figsize=(14, 10))
gs = fig.add_gridspec(4, 1, height_ratios=[2, 2, 2, 0.8])

# 子图1：各层结构 S
ax1 = fig.add_subplot(gs[0])
lines_S = []
for n in range(N_level):
    l, = ax1.plot(t, S[n], label=levels[n])
    lines_S.append(l)
ax1.set_title('各层结构 S 演化（嵌套系统）')
ax1.legend()
ax1.grid(True)
ax1.set_ylim(-0.1, 1.2)

# 子图2：张力 |E-I|
ax2 = fig.add_subplot(gs[1])
lines_tension = []
for n in range(N_level):
    tension = np.abs(E[n] - I[n])
    l, = ax2.plot(t, tension, label=levels[n])
    lines_tension.append(l)
line_c1 = ax2.axhline(init_S_c, c='orange', label='进化阈值')
line_c2 = ax2.axhline(init_S_c2, c='red', label='崩溃阈值')
ax2.set_title('张力 |E-I|')
ax2.legend()
ax2.grid(True)
ax2.set_ylim(-0.1, 2.5)

# 子图3：顶层（地球）动力学
ax3 = fig.add_subplot(gs[2])
line_S_top, = ax3.plot(t, S[-1], 'b-', label='地球结构 S')
line_I_top, = ax3.plot(t, I[-1], 'r-', label='内旋 I')
line_E_top, = ax3.plot(t, E[-1], 'g-', label='外扰 E')
ax3.set_title('顶层（地球）完整动力学')
ax3.legend()
ax3.grid(True)
ax3.set_ylim(-0.1, 3.0)

# 子图4：滑块控件
ax_k = fig.add_axes([0.15, 0.06, 0.65, 0.03])
ax_D = fig.add_axes([0.15, 0.02, 0.65, 0.03])
ax_Sc = fig.add_axes([0.15, -0.02, 0.65, 0.03])
ax_Sc2 = fig.add_axes([0.15, -0.06, 0.65, 0.03])

slider_k = Slider(ax=ax_k, label='耦合强度 k', valmin=0, valmax=1.0, valinit=init_k)
slider_D = Slider(ax=ax_D, label='耗散系数 D', valmin=0, valmax=0.1, valinit=init_D)
slider_Sc = Slider(ax=ax_Sc, label='进化阈值 S_c', valmin=0.5, valmax=1.5, valinit=init_S_c)
slider_Sc2 = Slider(ax=ax_Sc2, label='崩溃阈值 S_c2', valmin=1.5, valmax=3.0, valinit=init_S_c2)

def update(val):
    k = slider_k.val
    D = slider_D.val
    S_c = slider_Sc.val
    S_c2 = slider_Sc2.val

    S_new, I_new, E_new = simulate(k, D, S_c, S_c2)

    # 更新结构 S
    for n in range(N_level):
        lines_S[n].set_ydata(S_new[n])
    # 更新张力
    for n in range(N_level):
        tension_new = np.abs(E_new[n] - I_new[n])
        lines_tension[n].set_ydata(tension_new)
    # 更新阈值线
    line_c1.set_ydata([S_c, S_c])
    line_c2.set_ydata([S_c2, S_c2])
    # 更新顶层
    line_S_top.set_ydata(S_new[-1])
    line_I_top.set_ydata(I_new[-1])
    line_E_top.set_ydata(E_new[-1])

    fig.canvas.draw_idle()

slider_k.on_changed(update)
slider_D.on_changed(update)
slider_Sc.on_changed(update)
slider_Sc2.on_changed(update)

# 保存按钮
ax_save = fig.add_axes([0.85, 0.06, 0.1, 0.04])
btn_save = Button(ax_save, '保存图片')

def save_plot(event):
    plt.savefig('structure_force_simulation.png', dpi=300, bbox_inches='tight')
    print("图片已保存为 structure_force_simulation.png")

btn_save.on_clicked(save_plot)

plt.tight_layout()
plt.show()

# 输出最终状态
print("\n【结构生力理论 - 优化版仿真结果】")
for n in range(N_level):
    ten = np.abs(E[n, -1] - I[n, -1])
    if ten < init_S_c:
        res = "稳定"
    elif ten < init_S_c2:
        res = "进化"
    else:
        res = "崩解/重构"
    print(f"{levels[n]}: 最终张力={ten:.2f} | 状态={res}")