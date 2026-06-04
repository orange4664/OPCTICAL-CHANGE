# Extracted Workflow from Source DOCX

Source: `我会按主论文A_2026-06-04-19-05-08.docx`

This file preserves the source-document text used to organize the `test1` project. It is not a polished report; see `docs/experimental_flow.md` and `docs/ppt_outline.md` for cleaned project materials.

## Core Selection

- Main paper A: MoSe2 excitonic beam steering in an active van der Waals metasurface.
- New method B: electrically tunable strong coupling in hybrid-2D excitonic metasurfaces.
- Core innovation C: upgrade a bare-exciton phased array into a gate-tunable exciton-polariton phased array for programmable beam steering.
- Supporting evidence: compare one-layer and two-layer TMD amplitude stability to show a route toward more stable amplitude-phase control.

## Full Extracted Text


我会按“主论文 A + 可迁移新方法 B + 我们的实验设计 C”重新筛选，不再只追炫概念。重点会放在能否像实验设计比赛一样讲清目标、装置、变量、测量、判据和创新。

我会把候选筛成几个“主实验 + 可迁移新方法”的组合，并优先看 2025–2026 光控/电控光场调控里能用 Python 验证的方案。重点避免创新点退化成换电极或多测一个量。

对，这次我按你说的“主论文 A + 新方法 B，把 B 挪到 A 上”重新筛，而不是再凭空拼概念。

我先给结论：最适合你们这个课程/实验设计竞赛口径的方案，我现在推荐这个：

主论文 A：MoSe₂ 激子超表面的 active beam steering

新方法 B：电控强耦合 / 双 TMD 幅相解耦

我们的创新：把裸激子相控阵升级成“电控强耦合极化激元相控阵”，实现更稳定的幅度—相位联合调控和可编程光束偏转。

最终题目可以叫：

基于电控强耦合 MoSe₂/WS₂ 激子超表面的可编程光束偏转实验设计

Electrically Programmable Beam Steering in a Strong-Coupling Hybrid-2D Excitonic Metasurface

这个方案最像“实验设计创新大赛”的题：有主论文、有新方法、有明确物理闭环、有测试方案、有 Python 建模图，而且不靠“我分几个局域电极”这种弱创新。

1. 我按“实验设计竞赛”标准重新筛的原则

这种题不能只是“我找到一篇论文讲一讲”。它要像一个小 proposal：

主论文已有清楚实验基础：别人已经证明某个二维材料体系能调光。

找一个新方法解决主论文短板：比如强耦合、幅相解耦、闭环优化、相位匹配成像。

把新方法挪到主论文体系上：形成一个新实验方案。

能自圆其说地测出来：有光路、电路、测量量、对照组。

能用 Python/MATLAB 先画趋势图：说明方案不是纯口嗨。

你之前上传的深度研究材料里也反复强调，这门课更看重“可追溯的物理操控链条、可信测试方案、基于文献再组合的新 idea”，而不是普通文献综述。deep-research-report (6)

2. 最推荐方案：强耦合增强的二维激子相控阵

主论文 A：MoSe₂ 激子超表面光束偏转

主论文：

Melissa Li, Claudio U. Hail, Souvik Biswas, Harry A. Atwater, “Excitonic beam steering in an active van der Waals metasurface,” Nano Letters, 2023.

这篇做了什么？

它用单层 MoSe₂ 的激子共振做 active van der Waals metasurface。通过调节激子的辐射和非辐射速率，动态控制反射光的幅度和相位分布，最终实现反射光束在 A exciton、B exciton 和 trion 共振附近，从  到  的光束偏转。换句话说，它已经把二维 TMD 激子做成了一个 excitonic phased array metasurface。

主论文的物理链条是：

它非常符合课程要求，因为它直接调控：

光的幅度；

光的相位；

光的波前；

光束传播方向。

主论文 A 的短板

主论文 A 的问题是：它主要依赖裸激子共振。

裸激子调控有一个典型难点：

相位变化和幅度损耗强耦合。

你想要较大的相位变化，通常要靠近激子吸收峰；但靠近吸收峰，反射强度会下降，偏转效率也会受影响。

所以它的短板可以归纳成：

这正好给我们留出创新空间。

新方法 B1：电控强耦合 hybrid-2D excitonic metasurface

新方法论文：

Tom Hoekstra, Jorik van de Groep, “Electrically tunable strong coupling in a hybrid-2D excitonic metasurface for optical modulation,” 2025.

这篇提供的新方法是：

把二维半导体激子和 non-local dielectric metasurface 结合，形成室温下可电控的 exciton-photon strong coupling。

它的关键结果是：通过 gate 改变自由载流子浓度，从而改变 exciton 的非辐射衰减率，让系统从 strong coupling 连续过渡到 weak coupling，并实验展示了 9.9 dB reflectance modulation。论文摘要还明确说，这类 hybrid-2D excitonic metasurface 可用于 active wavefront manipulation 和 optical communication。

这个方法解决的是主论文 A 的短板：

也就是把“裸激子相位调控”升级为“强耦合极化激元相位调控”。

新方法 B2：双 TMD 幅度—相位解耦

还有一个今年更新的思路也很有用：

Tom Hoekstra, Mark L. Brongersma, Jorik van de Groep, “Hybrid-2D Excitonic Metasurfaces for Complex Amplitude Modulation,” 2026.

这篇提出用 hybrid-2D excitonic metasurface 做独立幅度和相位控制。它指出，普通动态相位调制常常会伴随散射幅度变化；他们用从实验提取的单层 WS₂ gate-tunable excitonic response 设计了保持近似均匀幅度的 -phase modulator，并进一步用第二层可调单层材料实现  全相位范围内的独立幅度和相位控制，用于 reconfigurable beam steering。

这篇是预印本，不要在 PPT 里说成“已发表顶刊”，但作为“今年的新方法灵感”很合适。

3. 我们的创新是什么？

我们的创新不是：

把全局调控变成局域电极。

这个太弱。

我们的创新应该写成：

把主论文 A 的裸 MoSe₂ 激子相控阵，升级为电控强耦合 hybrid-2D exciton-polariton 相控阵；再引入双 TMD 幅相解耦思路，使每个单元的复反射系数  可以更稳定地被 gate 调控，从而实现更高效率、更可编程的光束偏转。

简化成一句话：

从 bare-exciton phased array 升级到 gate-tunable exciton-polariton phased array。

这就不是简单换实验装置，而是换了调控机制。

4. 物理原理怎么讲？

4.1 单元响应：强耦合模型

每个 meta-atom / pixel 可以用一个耦合振子模型表示：

其中：

：metasurface 光学模式频率；

：TMD exciton 频率；

：光-物质耦合强度；

：光学模式损耗；

：gate-dependent exciton 非辐射衰减。

当 gate 改变载流子浓度时：

强耦合会逐渐变弱，反射谱和反射相位会改变：

这就是我们的电控机制。

4.2 多个单元组成相位梯度

每个位置  的反射单元有自己的电压：

对应复反射系数：

如果我们希望反射光偏到角度 ，就让相位满足：

远场光强由阵列因子决定：

这样：

这条链很清楚，适合比赛式汇报。

5. 实验方案怎么设计？

样品结构

画一个反射式器件：

non-local dielectric metasurface

hBN / monolayer MoSe₂ or WS₂ / hBN

transparent top gate or patterned local gates

bottom gate / substrate

如果想讲“双 TMD 幅相解耦”，可以画成：

hBN / WS₂ / hBN / MoSe₂ / hBN + gate

但 PPT 里别讲得太复杂。主线可以先是 single-TMD strong coupling，创新拓展再讲 dual-TMD amplitude compensation。

光路

实验光路非常清楚：

测试步骤：

先测反射谱扫波长和 gate voltage，得到 。

提取复反射系数用模型拟合 。

设计目标偏转角给定 ，计算目标相位梯度 。

反查电压分布从  反推每个单元的 。

测远场偏转在 Fourier plane 里看反射光主峰是否移到目标角度。

这很像实验设计比赛，因为它有完整的“设计—预测—测量—验证”闭环。

6. Python / MATLAB 可以模拟什么？

这个方案非常适合 Python。你不需要 COMSOL。

模拟 1：强耦合反射谱随 gate 变化

用耦合振子模型生成：

预期图：

低载流子浓度：strong coupling，反射谱有 upper/lower polariton 特征；

高载流子浓度： 变大，强耦合被破坏；

反射谱的峰位、深度和相位都变化。

图名：

Gate-tunable strong-to-weak coupling

模拟 2：单个像素的复反射系数

从反射模型提取：

画三张小图：

vs ；

vs ；

vs  复平面轨迹。

图名：

Gate-controlled complex reflection coefficient

这张图是核心，因为课程要求里明确有幅度调控和相位调控。

模拟 3：目标角度对应的电压分布

设目标偏转角：

计算目标相位：

然后从  曲线反查：

图名：

Inverse-designed gate voltage profile

这张图体现“实验设计”味道：不是只看现象，而是根据目标光学状态反推控制量。

模拟 4：远场光束偏转

用阵列因子：

画：

预期：

无相位梯度：主峰在 ；

设计 ：主峰在 ；

设计 ：主峰在 。

图名：

Electrically programmable beam steering

可选模拟 5：单层 vs 双层 TMD 幅相解耦对比

这是加分图。

对比：

single TMD：相位变化时  大幅波动；

dual TMD / strong-coupling design：在较大相位范围内  更稳定。

图名：

Amplitude-compensated phase modulation

这个图能解释为什么我们的方案不只是复述主论文。

7. 这个方案的 PPT 结构

第 1 页：主论文 A

标题：

Excitonic beam steering in active van der Waals metasurfaces

内容：

主论文用 monolayer MoSe₂ 激子做 active phased array；

已实现反射光束  到  偏转；

但裸激子调相位时幅度损耗难避免。

第 2 页：新方法 B

标题：

New method: electrically tunable strong coupling

内容：

hybrid-2D excitonic metasurface 可以在室温下实现 gate-tunable exciton-photon strong coupling；

gate 通过改变 exciton 非辐射衰减，使系统从 strong coupling 转到 weak coupling；

已展示 9.9 dB 反射调制。

第 3 页：我们的创新实验设计

标题：

Our proposal: polaritonic phased array

核心图：

三条创新点：

用强耦合极化激元替代裸激子作为调制单元；

目标是更稳定的复反射系数 ；

用反向设计从目标角度求 gate voltage map。

第 4 页：Python 模拟结果

放四张图：

；

vs ；

vs pixel index；

far-field beam steering。

第 5 页：测试方案 + 总结

测试方案：

tunable laser → polarizer → sample → Fourier-plane imaging → CCD

source meter / gate array 提供电控

总结：

本方案把新方法 B 的电控强耦合机制移植到主论文 A 的激子 beam steering 体系中，实现对反射光幅度、相位和传播方向的电控。

8. 还有哪些备选组合？

我再给你三个备选，按“能不能讲成实验设计”排序。

备选 1：双栅 WSe₂ SHG + PRL 面内电场激子混合

主论文 A

Cha et al., “Enhancing resonant second harmonic generation in bilayer WSe₂ by layer-dependent exciton-polaron effect,” 2024.

它做的是双栅 bilayer WSe₂，通过 layer-dependent exciton-polaron effect 实现约 40 倍 resonant SHG 增强，而且只用接近击穿阈值约 3% 的低电场。

新方法 B

Bairen Zhu et al., “In-Plane Electric Field Induced Orbital Hybridization of Excitonic States in Monolayer WSe₂,” PRL 2023.

它证明面内电场可以让 WSe₂ 中 Rydberg exciton 的 2s/2p 态发生 orbital hybridization，使原本暗的 2p exciton 变得 optically active，并增强高激发态振子强度。

我们的创新

把 B 的面内电场激子态混合挪到 A 的双栅 bilayer WSe₂ SHG体系里，做一个“三电极/正交电场”方案：

最终实现：

优点：物理很漂亮，电控味很强。

缺点：比 MoSe₂ beam steering 更偏激子物理，4–5 分钟不容易讲清。

备选 2：3R-MoS₂ 准相位匹配 + 超快时空成像

主论文 A

Nature Photonics 2025, “Quasi-phase-matched up- and down-conversion in periodically poled layered semiconductors.”

这篇把传统周期极化/准相位匹配移植到 3R-MoS₂ 中，在 3.4 μm、3 个极化周期内实现 0.03% 的频率转换效率，并展示 telecom 波段 SPDC 光子对。

新方法 B

Nature Nanotechnology 2025, “Spatiotemporal imaging of nonlinear optics in van der Waals waveguides.”

这篇提出远场超快成像方法，可以追踪 vdW waveguide 中基频光和谐波光传播，具有飞秒和 sub-50 nm 时空精度，并能无先验材料光学常数地确定相位匹配角、模式和损耗。

我们的创新

把 B 的时空成像诊断方法挪到 A 的periodically poled 3R-MoS₂ 上，做一个“可视化优化准相位匹配”的实验设计：

优点：顶刊味最强。

缺点：它更像“测量与优化方法”，不是很直接的光控/电控光学状态调控，容易偏离作业主线。

备选 3：3R-MoS₂ qBIC SHG + 非局域 metasurface 增强

主论文 A

npj Nanophotonics 2025, “Ultrafast all-optical switching in nonlinear 3R-MoS₂ van der Waals metasurfaces.”

这篇展示 3R-MoS₂ qBIC metasurface 的 SHG 增强超过 ，并用 degenerate pump-probe 实现近 unity modulation depth 的超快 SHG 偏振切换。

新方法 B

Nature Photonics 2025, “3R-stacked transition metal dichalcogenide non-local metasurface for efficient second-harmonic generation.”

这篇用非局域光学共振绕开相位匹配限制，在 160 nm 厚 3R-MoS₂ metastructure 中实现约 140 倍 SHG 增强和约  的单次通过效率。

我们的创新

把 B 的非局域高效率 SHG metastructure挪到 A 的全光超快偏振切换框架里，目标是：

优点：文献很新，顶刊味强。

缺点：创新点有点像“把两个强机制相加”，实验设计不如主推荐方案清楚。

9. 最终我建议你选哪个？

我建议最终选：

基于电控强耦合 MoSe₂/WS₂ 激子超表面的可编程光束偏转实验设计

原因很简单：

它最贴合作业要求：电控、幅度、相位、波前、二维 TMD。

它不像 SHG 那么难讲，也不像 qBIC 结构光那么抽象。

它符合“主论文 + 新方法挪用”的创新逻辑。

Python 建模最容易做出漂亮图。

答辩时很好解释：原来是裸激子相控阵，我们把它升级成强耦合极化激元相控阵。

10. 最后一版核心流程

你可以直接按这个说：

主论文 A：MoSe₂ active vdW metasurface 已经实现 excitonic beam steering，说明二维 TMD 激子可以调控反射光的幅度和相位。

问题：裸激子调相位时伴随吸收，幅度和相位难以独立控制，偏转效率受限。

新方法 B：2025 hybrid-2D excitonic metasurface 证明可以用 gate 实现电控强耦合，并获得 9.9 dB 反射调制；2026 新方法进一步提出双 TMD 幅相解耦。

我们的创新：把 B 的强耦合/幅相解耦机制挪到 A 的 beam steering 实验上，设计一个电控 exciton-polariton phased array。

基本原理：gate 改变 exciton 线宽和强耦合状态，进而改变每个单元的复反射系数 ；多个单元形成相位梯度，实现光束偏转。

测试方案：可调谐激光入射，源表加 gate，Fourier-plane camera 测远场反射角。

Python 模拟：耦合振子模型算  和 ，反向设计  电压图，阵列因子算  光束偏转。

这就是最清楚、最像实验设计创新赛、也最适合 4–5 分钟 PPT 的版本。
