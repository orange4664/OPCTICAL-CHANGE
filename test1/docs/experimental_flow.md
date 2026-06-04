# Experimental Flow

## 目标

设计一个电控可编程 excitonic metasurface，通过 gate voltage 调节每个 metapixel 的 complex reflection coefficient，使反射光在目标角度形成主瓣。这个方案的重点不是复现主论文图，而是把已验证的 electrically tunable strong coupling 机制移植到 excitonic beam steering 场景中。

## 物理链条

主论文 A 已经证明 monolayer MoSe2 active vdW metasurface 可以调控反射波前。这里的升级点是把 bare-exciton 调制单元替换为 gate-tunable exciton-polariton 单元：

`Vg -> gamma_x(Vg) -> r(Vg)=|r|exp(i phi) -> phi_j=k0 x_j sin(theta0) -> far-field peak at theta0`

其中 `gamma_x(Vg)` 表示 gate-induced exciton linewidth / non-radiative decay，`r(Vg)` 是每个像素的复反射系数，`phi_j` 是阵列位置 `x_j` 对应的目标相位。

## 器件概念

主线结构：

- non-local dielectric metasurface
- hBN encapsulation
- monolayer MoSe2 or WS2
- transparent top gate or patterned local gates
- bottom gate / substrate

支撑分析：

- hybrid-2D complex amplitude modulation 文献说明 amplitude-phase trade-off 是实际器件设计里必须处理的问题。
- 当前第五张图不再使用手工 one-layer/two-layer 补偿曲线，而是回到同一 coupled-oscillator model，比较不同工作能量下 phase span 与 amplitude CV 的取舍。
- 这仍然是设计模拟，不作为主创新替代项。

## 测量流程

1. 用 tunable laser 扫 photon energy，并同步扫 gate voltage，得到 `R(E,Vg)`。
2. 用 coupled-oscillator model 拟合或解释谱线变化，提取 design energy 下的 `r(Vg)`。
3. 选择目标偏转角，例如 `0/10/20 deg`。
4. 用 `phi_j=k0 x_j sin(theta0)` 生成目标相位梯度。
5. 通过 `r(Vg)` 的相位反查每个 metapixel 的 gate voltage。
6. 在 Fourier plane 中测 reflected far field，检查主瓣是否移动到目标角。

## Python 预验证

Python 模拟检查五件事：

- gate voltage 是否能把 coupled-oscillator reflection map 从清晰强耦合特征推向高损耗弱耦合状态
- design energy 下 `r(Vg)` 是否提供可用的 amplitude / phase 控制窗口
- 目标角是否能反推出可施加的 gate-voltage profile
- 由这些 voltage 选出的 phase profile 是否能在 array factor 中产生目标 far-field peak
- 不同工作能量是否提供不同的 phase-amplitude trade-off，从而指导 design energy 选择

## 判据

项目级判据是机制链自洽，而不是声称实验已经实现。当前 Python 结果给出：

- target `0 deg` 对应 far-field peak `0.0 deg`
- target `10 deg` 对应 far-field peak about `10.0 deg`
- target `20 deg` 对应 far-field peak about `20.1 deg`
- Figure 5 给出工作能量选择中的 phase span / amplitude CV 取舍，避免把手工补偿曲线当成仿真证据

## 边界

模拟使用代表性、物理可解释参数；它不是 measured spectra、不是 COMSOL/FDTD full-wave calculation，也不声称达到文献中的 9.9 dB modulation 或任何已发表器件效率。正式文献身份、数字和措辞边界见 [`literature_notes.md`](literature_notes.md)。
