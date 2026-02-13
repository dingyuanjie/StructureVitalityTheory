import numpy as np
import matplotlib.pyplot as plt

# ======================
# 结构生力理论 - 多层嵌套仿真
# 层级：0=细胞, 1=人, 2=社会, 3=文明, 4=地球
# ======================

np.random.seed(42)

# 基础参数
dt = 0.01
total_steps = 500
k = 0.6       # 耦合强度
D = 0.02      # 耗散系数
S_c = 1.0     # 一级阈值（稳定→进化）
S_c2 = 2.0    # 二级阈值（进化→崩溃）

# 5层嵌套
levels = ['细胞', '人', '社会', '文明', '地球']
N_level = len(levels)

# 初始化数组
S = np.zeros((N_level, total_steps))
I = np.zeros((N_level, total_steps))
E = np.zeros((N_level, total_steps))
t = np.arange(total_steps) * dt

# 初始状态
for n in range(N_level):
    S[n, 0] = 1.0
    I[n, 0] = 1.0

# 外层 = 内层的外扰
# 第 n 层的外扰 E[n] = 上一层 S[n+1] + 噪声
# 最顶层外扰来自外部环境

for i in range(1, total_steps):
    # 最顶层（地球）外扰
    E[-1, i] = 1.5 + 0.2*np.sin(0.05*i) + 0.1*np.random.randn()

    # 从上往下更新
    for n in range(N_level-2, -1, -1):
        E[n, i] = S[n+1, i-1] + 0.05*np.random.randn()

    # 更新每一层
    for n in range(N_level):
        # 内旋 = 历史积分
        I[n, i] = I[n, i-1] + 0.01 * S[n, i-1]
        # 结构生力主方程
        dS = k * (E[n, i] - I[n, i]) * dt - D * S[n, i-1] * dt
        S[n, i] = S[n, i-1] + dS
        # 防止负数
        S[n, i] = max(S[n, i], 0.0)

# ======================
# 绘图
# ======================
fig, axes = plt.subplots(3, 1, figsize=(12, 9))

# 1. 各层结构 S 演化
for n in range(N_level):
    axes[0].plot(t, S[n], label=f'{levels[n]}')
axes[0].set_title('各层结构 S 演化（嵌套系统）')
axes[0].legend()
axes[0].grid(True)

# 2. 张力 |E-I|
for n in range(N_level):
    tension = np.abs(E[n] - I[n])
    axes[1].plot(t, tension, label=f'{levels[n]}')
axes[1].axhline(S_c, c='orange', label='进化阈值')
axes[1].axhline(S_c2, c='red', label='崩溃阈值')
axes[1].set_title('张力 |E-I|')
axes[1].legend()
axes[1].grid(True)

# 3. 最顶层（地球）演示
axes[2].plot(t, S[-1], 'b-', label='地球结构 S')
axes[2].plot(t, I[-1], 'r-', label='内旋 I')
axes[2].plot(t, E[-1], 'g-', label='外扰 E')
axes[2].set_title('顶层（地球）完整动力学')
axes[2].legend()
axes[2].grid(True)

plt.tight_layout()
plt.show()

# 输出结论
print("\n【结构生力理论 - 多层嵌套仿真结果】")
for n in range(N_level):
    ten = np.abs(E[n, -1] - I[n, -1])
    if ten < S_c:
        res = "稳定"
    elif ten < S_c2:
        res = "进化"
    else:
        res = "崩解/重构"
    print(f"{levels[n]}: 最终张力={ten:.2f} | 状态={res}")