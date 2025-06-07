
# 📐 核心公式与推导（Core Equations & Derivations）

> 本节将系统整理“结构生力理论”的关键数学公式、几何结构关系、变量定义、推导路径，以及与现有物理理论（如量子力学、相对论）之间的异同。  
> This section systematically organizes the key mathematical formulas, geometric structures, variable definitions, derivation paths, and comparisons with existing physical theories (e.g., quantum mechanics and relativity) in the theory of Structural Vital Force.

---

## 一、基础变量定义（Basic Variable Definitions）

| 变量 (Variable) | 含义 (Meaning) | 单位 (Unit) |
|----------------|----------------|-------------|
| \( T \)        | 结构周期 / Structural Period | s |
| \( \theta \)   | 结构角 / Structural Angle     | ° or rad |
| \( r \)        | 结构半径 / Structural Radius  | m |
| \( m_{\text{eff}} \) | 有效质量 / Effective Mass | kg |
| \( V_s \)      | 结构势能 / Structural Potential Energy | J |
| \( \hbar_s \)  | 等效结构普朗克常数 / Structural Planck Constant | J·s |

---

## 二、结构周期公式（Structural Period Formula）

\[
T_n = T_0 \cdot n^\alpha \cdot \cos^\beta(\theta_n)
\]

- \( T_0 \): 基准周期 / Base period  
- \( n \): 结构层级 / Structural layer (analogous to quantum number)  
- \( \alpha, \beta \): 结构生力指数参数 / Structural exponents  
- \( \theta_n \): 第 \( n \) 层结构角 / Structural angle at level \( n \)

---

## 三、结构势能表达式（Structural Potential Energy）

\[
V_s(n) = -\frac{A}{n^\gamma} \cdot \cos(\theta_n) \cdot \exp(-\delta \cdot n)
\]

- \( A \): 耦合强度常数 / Coupling constant  
- \( \gamma \): 结构衰减因子 / Decay exponent  
- \( \delta \): 结构压缩扰动因子 / Structural compression factor  

> 当 \( \theta_n \approx 137.5^\circ \) 时，对应最稳定结构态。  
> The most stable structure appears when \( \theta_n \approx 137.5^\circ \).

---

## 四、等效结构普朗克常数（Effective Structural Planck Constant）

\[
\hbar_s(n) = \hbar \cdot \left(1 + \epsilon \cdot \cos(\theta_n)\right)
\]

- \( \epsilon \): 结构耦合系数 / Structural coupling coefficient

\[
\Delta E = \hbar_s \cdot \omega = \frac{2\pi \hbar_s}{T_n}
\]

> 该项用于替代传统跃迁中的普朗克常数。  
> This replaces the conventional Planck constant in transition energy calculations.

---

## 五、结构跃迁能级拟合公式（Transition Energy for Hydrogen-like Systems）

\[
E_n = -\frac{m_{\text{eff}} \cdot (c \cdot \cos\theta_n)^2}{2n^2}
\]

> 模拟玻尔模型，但引入结构角扰动项以增强拟合能力。  
> Similar to the Bohr model, but enhanced with structural angular modulation.

---

## 六、结构三角对称模型（Triangle Symmetry Model）

基本结构角组成一个稳定结构三角形：

- 黄金角：\( \theta_\phi \approx 137.5^\circ \)  
- 辅助角：\( \theta_s \approx 85^\circ \)

构成三角形（组成总角度 \( \approx 360^\circ \)）：

∠A = 137.5°  
∠B = 137.5°  
∠C = 85°  

> 用于描述普朗克尺度至原子轨道间的嵌套关系。  
> Used to describe the nested scaling from Planck scale to atomic orbits.

---

## 七、结构映射关系（Structure-Scale Mapping）

\[
r_n = v_s \cdot T_n
\]

- \( v_s \): 结构传播速度（可能小于或大于光速）  
- \( T_n \): 第 \( n \) 层周期  
> 用于连接微观结构、日常尺度与天文尺度的桥梁。  
> Acts as a bridge across microscopic, human-scale, and cosmic structures.

---

## 八、与现有理论的对比（Comparison with Existing Theories）

| 项目 (Aspect)       | 结构生力理论 (Structural Vital Force) | 传统理论（玻尔模型等） (Conventional Models) |
|---------------------|-----------------------------------------|-----------------------------------------------|
| 基本量纲 (Base Unit) | 结构周期、结构角 (T, θ)                | 普朗克常数、轨道半径 (ℏ, r)                   |
| 能量来源 (Energy Source) | 内旋扰动与角耦合 (inner spin field) | 库仑势、角动量量子化 (Coulomb + quantization) |
| 对称结构 (Symmetry) | 螺旋结构 + 三角耦合                   | 球对称 + 波函数                               |
| 推导路径 (Derivation) | 三角结构嵌套与比例律                  | 哈密顿量 + 波动方程                           |

---

## 🚧 后续方向建议（Future Directions）

- 将本公式体系应用于其他原子系统（如氦、锂）进行拟合验证  
- 构建“结构周期-频谱”数据库  
- 与天文尺度的结构周期对照寻找尺度同构证据  
- 编写用于验证公式的 Python / Mathematica 脚本

> 如需完整图示、数据拟合结果，请参见 `/visuals` 与 `/data` 文件夹。  
> For full illustrations and fitting results, see `/visuals` and `/data` folders.
