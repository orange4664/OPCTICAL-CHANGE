# PPT-Ready Outline

## Title

基于电控强耦合 MoSe2/WS2 激子超表面的可编程光束偏转实验设计

Electrically Programmable Beam Steering in a Strong-Coupling Hybrid-2D Excitonic Metasurface

## Slide 1: 主论文 A 与短板

**一句话：** MoSe2 excitonic metasurface 已经能做反射光束偏转，但 bare-exciton 调相位时幅度损耗会限制控制窗口。

- 主论文：Li, Hail, Biswas, Atwater, *Nano Letters* 2023。
- 已有结果：active vdW metasurface 动态控制 reflection amplitude / phase / wavefront，并实现约 `-30 deg` 到 `+30 deg` 的 reflected beam steering。
- 问题切入：靠近 exciton resonance 获得相位变化时，吸收和幅度下降会一起出现。
- 本页图：可以用源 PDF 的逻辑图，或只放“主论文 A -> limitation”的简洁流程。

## Slide 2: 新方法 B

**一句话：** gate-tunable strong coupling 提供了比 bare exciton 更强的电控机制。

- B1：Hoekstra and van de Groep, *Light: Science & Applications* 2026；2025 arXiv 预印本历史。
- 关键机制：gate voltage 改变 carrier density / exciton linewidth，使系统经历 strong-to-weak coupling transition。
- 已核验背景数字：该光调制器件报道 9.9 dB reflectance modulation；这里只作为机制依据，不说成我们的结果。
- B2：Hoekstra, Brongersma, van de Groep, *Nano Letters* 2026，用作 amplitude-phase control 支撑。

## Slide 3: 我们的创新 C

**一句话：** 把主论文 A 的 bare-exciton phased array 升级为 gate-tunable exciton-polariton phased array。

- 每个 metapixel 的控制量从单纯 exciton resonance 变成 `r(Vg)=|r|exp(i phi)`。
- 目标角 `theta0` 先转为相位梯度 `phi_j=k0 x_j sin(theta0)`。
- 再通过 `r(Vg)` 的相位响应反查 gate-voltage map。
- 本页核心图：机制链 `Vg -> gamma_x -> r(Vg) -> phase gradient -> far-field peak`。

## Slide 4: Python 模拟结果

**一句话：** 五张 Python 图证明这个设计链条在模型内是连贯的。

- 放 `figure_1_strong_coupling_gate_tuning`: gate-tuned coupled-oscillator map。
- 放 `figure_2_complex_reflection_coefficient`: complex reflection path、amplitude、phase。
- 放 `figure_3_inverse_gate_profile`: 0/10/20 deg 的 voltage profile。
- 放 `figure_4_programmable_beam_steering`: far-field peak 跟随目标角。
- 放 `figure_5_amplitude_compensation`: one-layer vs two-layer amplitude-stability 支撑图。

讲法顺序：先说“电压能调单元响应”，再说“单元响应能反推出阵列电压”，最后说“阵列电压在 far field 给出目标主瓣”。

## Slide 5: 实验验证与结论

**一句话：** 这是一个 design-prediction-control-measurement-verification loop。

- 样品：non-local dielectric metasurface + hBN/TMD/hBN + gate stack。
- 光路：tunable laser -> polarizer/objective -> electrically addressable sample -> Fourier-plane imaging -> CCD/sCMOS。
- 电控：source meter 或 gate array 给 metapixel 施加 voltage profile。
- 判据：Fourier plane 中主瓣从 `0 deg` 移到设定角，且 amplitude loss 得到控制或由 two-layer 支撑方案改善。
- 结论：电控强耦合可以把 excitonic beam steering 从 bare-exciton tuning 推进到可编程 exciton-polariton wavefront control。

## 不要这样说

- 不说 Python 图是实验数据。
- 不说本项目已经实现 9.9 dB modulation。
- 不把 two-layer amplitude compensation 说成主创新；它是支撑图。
