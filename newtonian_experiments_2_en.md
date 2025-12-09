# 牛顿力学级可验证实验：结构生力理论探索  

## 实验一：桁架结构受力分布优化验证实验  
### （一）实验背景（Experimental Background）  
在牛顿力学中，结构的受力分布遵循静力学平衡与材料力学定律。结构生力理论推测，**通过特定的桁架拓扑结构设计，可主动引导力的传递路径，使结构在相同载荷下应力分布更均匀**。本实验通过对比不同桁架结构在集中载荷下的应变数据，验证结构对力传递的调控作用。  

In Newtonian mechanics, structural force distribution adheres to static equilibrium and material mechanics laws. The Structural Generative Force Theory hypothesizes that **specific truss topology designs can actively guide force transmission paths, resulting in more uniform stress distribution under the same load**. This experiment compares strain data of different truss structures under concentrated loads to verify structural control over force transfer.  


### （二）实验原理（Experimental Principle）  
制备三组几何尺寸相同但拓扑结构不同的桁架模型：**正三角形桁架**、**菱形桁架**和**分形递归桁架**。在桁架顶端施加恒定垂直载荷F，根据结构生力理论，分形递归桁架的自相似结构能通过多级分支分散应力，降低关键节点的应力集中。通过应变片测量各节点应变ε，对比应力分布差异。  

Fabricate three truss models with identical dimensions but different topologies: **equilateral triangle truss**, **diamond truss**, and **fractal recursive truss**. Apply a constant vertical load F at the top. The fractal truss’s self-similar structure is predicted to disperse stress through hierarchical branching, reducing stress concentration at key nodes. Measure strain ε at each node using strain gauges and compare stress distributions.  


### （三）实验步骤（Experimental Steps）  
#### 1. 桁架模型制备（Truss Model Preparation）  
- 材料：采用3D打印尼龙材料（弹性模量E = 2.8 GPa，密度ρ = 1.15 g/cm³）。  
- 尺寸：底边跨度L = 30 cm，高度H = 20 cm，杆件直径d = 2 mm。  
- 结构参数：  
  - 正三角形桁架：等边单元重复排列；  
  - 菱形桁架：菱形单元（内角60°/120°）组合；  
  - 分形递归桁架：基于Sierpinski三角形，迭代3次。  

- Material: 3D-print with nylon (elastic modulus E = 2.8 GPa, density ρ = 1.15 g/cm³).  
- Dimensions: Bottom span L = 30 cm, height H = 20 cm, bar diameter d = 2 mm.  
- Structural parameters:  
  - Equilateral triangle truss: Repeated equilateral units;  
  - Diamond truss: Combined diamond units (60°/120° angles);  
  - Fractal recursive truss: Sierpinski triangle, 3-level iteration.  


#### 2. 测试平台搭建（Testing Setup）  
- 将桁架底端固定在刚性基座上，顶端中心连接力传感器（量程0 - 50 N，精度0.01 N）。  
- 在各杆件中部及节点处粘贴**电阻应变片**（灵敏度系数2.0 ± 0.01），连接动态应变仪实时采集数据。  

- Fix the truss base on a rigid platform; attach a load cell (range 0 - 50 N, accuracy 0.01 N) at the top center.  
- Paste **resistive strain gauges** (gauge factor 2.0 ± 0.01) on bar midpoints and nodes, connect to a dynamic strain indicator for real-time data collection.  


#### 3. 数据采集与分析（Data Collection and Analysis）  
- 逐级施加载荷F = 5 N、10 N、15 N，每个载荷保持30秒，记录应变数据。  
- 计算各结构的**应力集中系数K**（K = 最大应力/平均应力），绘制应力云图对比分析。  

- Apply loads F = 5 N, 10 N, 15 N incrementally, hold each load for 30 s, and record strain data.  
- Calculate the **stress concentration factor K** (K = max stress/average stress) for each structure; plot stress contour maps for comparison.  


### （四）预期结果（Expected Results）  
- 分形递归桁架的应力集中系数K显著低于正三角形与菱形桁架（降低20% - 30%），验证其通过结构设计优化力传递的理论假设。  
- 随着载荷增加，分形桁架的应变分布更接近均匀状态，符合“结构生力”对力场调控的预测。  

- The fractal recursive truss’s stress concentration factor K is 20% - 30% lower than the other trusses, validating the hypothesis of force transfer optimization via structure.  
- As load increases, the fractal truss exhibits a more uniform strain distribution, consistent with the theory’s prediction of force field control.  


---  

## 实验二：复合旋转摆的摆动周期差异实验  
### （一）实验背景（Experimental Background）  
单摆周期公式T = 2π√(L/g) 描述了摆长与重力加速度对周期的影响。结构生力理论推测，**具有复合嵌套结构的摆锤在摆动过程中，因内部结构的相对运动产生附加惯性力，将改变摆动周期**。本实验通过对比不同复合摆与传统单摆的周期，验证结构对动力学特性的影响。  

The simple pendulum formula T = 2π√(L/g) describes the influence of length and gravity on period. The Structural Generative Force Theory hypothesizes that **compound nested pendulum bobs generate additional inertial forces due to internal relative motion during oscillation, altering the period**. This experiment compares periods of compound pendulums and simple pendulums to verify structural effects on dynamic properties.  


### （二）实验原理（Experimental Principle）  
设计两种复合摆：**双球嵌套摆**（内球可自由转动）和**螺旋叶片摆**（叶片随摆动产生空气动力学力矩），与传统单球摆对比。根据理论，复合摆的内部结构运动会引入附加力矩M，改变等效转动惯量I，进而影响摆动周期T。通过高精度计时器记录摆动100次的总时间t，计算平均周期T = t/100。  

Design two compound pendulums: **double-sphere nested pendulum** (inner sphere free to rotate) and **spiral vane pendulum** (vanes generate aerodynamic torque during swing), compared to a simple single-sphere pendulum. Internal motion of compound pendulums introduces additional torque M, altering the effective moment of inertia I and period T. Record the total time t for 100 oscillations using a high-precision timer; calculate the average period T = t/100.  


### （三）实验步骤（Experimental Steps）  
#### 1. 摆锤制备（Pendulum Bob Preparation）  
- **传统单球摆**：直径3 cm、质量50 g的实心钢球；  
- **双球嵌套摆**：外球直径4 cm（空心），内球直径2 cm（可自由转动），总质量50 g；  
- **螺旋叶片摆**：4片螺旋状亚克力叶片（螺距10 cm，结构角45°），总质量50 g。  

- **Simple single-sphere pendulum**: 3 cm-diameter, 50 g solid steel ball;  
- **Double-sphere nested pendulum**: 4 cm-diameter outer sphere (hollow), 2 cm-diameter inner sphere (free-rotating), total mass 50 g;  
- **Spiral vane pendulum**: 4 acrylic spiral vanes (pitch 10 cm, structural angle 45°), total mass 50 g.  


#### 2. 实验装置搭建（Experimental Setup）  
- 所有摆的摆长L统一设置为1 m（误差 < 1 mm），悬挂于无摩擦轴承支架上。  
- 使用光电门传感器（精度10⁻⁵ s）自动记录摆动次数与时间。  

- Set pendulum length L = 1 m (error < 1 mm) for all pendulums; suspend from frictionless bearing supports.  
- Use photogate sensors (10⁻⁵ s accuracy) to automatically record oscillation counts and time.  


#### 3. 数据采集与分析（Data Collection and Analysis）  
- 每种摆进行**20组独立实验**，每次摆动幅度控制在5°以内（减少非线性误差）。  
- 计算周期平均值与标准差，通过单因素方差分析（ANOVA）检验组间差异显著性（p < 0.05）。  

- Conduct **20 independent trials** for each pendulum; limit swing amplitude to ≤5° (reduce nonlinear errors).  
- Calculate mean periods and standard deviations; perform one-way ANOVA to test significant differences (p < 0.05).  


### （四）预期结果（Expected Results）  
- 双球嵌套摆与螺旋叶片摆的周期显著偏离传统单摆理论值（偏差 > 5%），且两种复合摆的周期存在差异，验证结构运动产生的附加力对动力学特性的影响。  
- 螺旋叶片摆因空气动力学效应，周期波动范围更大，符合“结构生力”对环境交互作用的预测。  

- The periods of compound pendulums deviate > 5% from the simple pendulum’s theoretical value, and the two compound types differ significantly, validating the impact of additional forces from structural motion.  
- The spiral vane pendulum exhibits greater period variability due to aerodynamic effects, consistent with the theory’s prediction of environmental interactions.  


---  

### 说明（Notes）  
1. **文件用途**：可直接保存为`newtonian_experiments_2.md`，上传GitHub作为牛顿力学级验证的扩展方案。  
2. **成本控制**：实验材料可选用3D打印耗材与基础力学元件，适合高校实验室或DIY科学项目。  
3. **理论延伸**：若结果支持假设，可进一步研究结构参数（如嵌套层数、叶片角度）与动力学特性的量化关系。  

### 英文版本（English Version）  
可直接复制上述内容（已包含中英对照），或单独提取英文部分保存为`newtonian_experiments_2_en.md`，便于国际学术交流。  

（注：实验设计基于理论逻辑推导，实际操作需严格控制变量、重复验证。若观测到与预期一致的结果，将为结构生力理论提供牛顿力学范畴的实证支持；若存在偏差，可优化实验设计或修正理论模型。）  