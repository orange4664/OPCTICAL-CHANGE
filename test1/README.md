# 基于电控强耦合 MoSe2/WS2 激子超表面的可编程光束偏转实验设计

**Electrically Programmable Beam Steering in a Strong-Coupling Hybrid-2D Excitonic Metasurface**

本文件夹是一个“创新实验设计 + Python 模拟验证”项目，不是对文献图片或 PDF 图示的复现。核心思路是把主论文中的 bare-exciton beam-steering metasurface 升级为电控 strong-coupling exciton-polariton phased array，并用可复现的 Python 模型检查从 gate voltage 到 far-field beam steering 的物理链条。

## 核心逻辑

- 主论文 A：Melissa Li 等人在 *Nano Letters* 2023 报道的 active vdW MoSe2 excitonic beam steering。
- 短板：bare exciton 调相位时容易伴随幅度损耗，复杂反射系数 `r=|r|exp(i phi)` 的控制窗口受限。
- 新方法 B1：hybrid-2D excitonic metasurface 中的 electrically tunable strong coupling，可通过 gate 改变 exciton non-radiative decay / linewidth。
- 支撑方法 B2：hybrid-2D complex amplitude modulation，说明双 TMD 结构可以作为改善 amplitude-phase control 的路线。
- 本项目创新 C：把 B1 的电控强耦合机制移植到 A 的 beam-steering 场景，设计 gate-tunable exciton-polariton phased array；B2 只作为第五张图的支撑证据，不替代主创新。

选择这个题目而不是备选 SHG/qBIC 组合，是因为它的“设计-预测-控制-测量-验证”闭环最清楚：电压调 exciton linewidth，linewidth 调 complex reflection，相位梯度调 far-field peak，Python 也能给出确定性的预测图。

## 已生成模拟图

运行 `scripts/make_figures.py` 会在 [`output/figures/`](output/figures/) 生成 PNG 和 PDF 两种格式：

1. [`figure_1_strong_coupling_gate_tuning.png`](output/figures/figure_1_strong_coupling_gate_tuning.png): gate-tuned coupled-oscillator reflection map。
2. [`figure_2_complex_reflection_coefficient.png`](output/figures/figure_2_complex_reflection_coefficient.png): design energy 下的 complex reflection path、amplitude 和 phase。
3. [`figure_3_inverse_gate_profile.png`](output/figures/figure_3_inverse_gate_profile.png): 0、10、20 deg 目标角对应的 inverse-designed gate-voltage profile。
4. [`figure_4_programmable_beam_steering.png`](output/figures/figure_4_programmable_beam_steering.png): array-factor far-field steering 结果。
5. [`figure_5_amplitude_compensation.png`](output/figures/figure_5_amplitude_compensation.png): one-layer 与 two-layer TMD amplitude-stability 支撑对比。

## 运行模拟

```powershell
python -m pip install -r requirements.txt
python scripts/make_figures.py --output-dir output/figures
pytest
```

## 模型参数和边界

模型采用 coupled oscillator + inverse phase lookup + 1D array factor。默认参数包括 `design_energy_ev=1.695`、`wavelength_m=710e-9`、`metapixel_count=96`、`metapixel_spacing_m=0.32e-6`、目标角 `0/10/20 deg`，并用 gate-dependent exciton linewidth 表示电控载流子引起的非辐射展宽。参数是为了让机制窗口清楚可见而选取的代表值，不是实验拟合值；文献中已核验的结论和数字单独记录在 [`docs/literature_notes.md`](docs/literature_notes.md)。

## 项目材料

- 源 Word 笔记：[`source/我会按主论文A_2026-06-04-19-05-08.docx`](source/我会按主论文A_2026-06-04-19-05-08.docx)
- 视觉流程 PDF：[`source/低维材料_图片合集.pdf`](source/低维材料_图片合集.pdf)
- 来源逻辑提取：[`source/extracted_workflow.md`](source/extracted_workflow.md)
- PDF 流程摘要：[`docs/visual_workflow.md`](docs/visual_workflow.md)
- 实验流程说明：[`docs/experimental_flow.md`](docs/experimental_flow.md)
- 文献核验笔记：[`docs/literature_notes.md`](docs/literature_notes.md)
- 4-5 分钟汇报大纲：[`docs/ppt_outline.md`](docs/ppt_outline.md)
- LaTeX 报告 PDF：[`report/test1_latex_report.pdf`](report/test1_latex_report.pdf)
- LaTeX 源文件：[`report/test1_latex_report.tex`](report/test1_latex_report.tex)
