# 基于电控强耦合 MoSe2/WS2 激子超表面的可编程光束偏转实验设计

**Electrically Programmable Beam Steering in a Strong-Coupling Hybrid-2D Excitonic Metasurface**

This folder develops an innovation proposal, not a figure reproduction. The core idea is to upgrade the bare-exciton beam-steering metasurface from the main paper into an electrically controlled strong-coupling exciton-polariton phased array, then use Python simulations to check the mechanism chain.

## Core Idea

- Main paper A: MoSe2 excitonic beam steering in an active van der Waals metasurface.
- Limitation: bare-exciton phase tuning can be coupled to amplitude loss.
- New method B: gate-tunable exciton-photon strong coupling in hybrid-2D excitonic metasurfaces.
- Proposed design C: use gate control to tune the complex reflection coefficient of each metapixel and form a programmable phase gradient for beam steering.
- Supporting panel: compare one-layer and two-layer TMD amplitude stability to show a route toward more stable amplitude-phase control.

## Source Materials

- Source Word note: [`source/我会按主论文A_2026-06-04-19-05-08.docx`](source/我会按主论文A_2026-06-04-19-05-08.docx)
- Visual workflow PDF: [`source/低维材料_图片合集.pdf`](source/低维材料_图片合集.pdf)
- Extracted source text: [`source/extracted_workflow.md`](source/extracted_workflow.md)
- Visual workflow summary: [`docs/visual_workflow.md`](docs/visual_workflow.md)
- Experiment flow: [`docs/experimental_flow.md`](docs/experimental_flow.md)
- Literature notes: [`docs/literature_notes.md`](docs/literature_notes.md)
- PPT-ready outline: [`docs/ppt_outline.md`](docs/ppt_outline.md)

## Planned Python Simulations

The simulation chain uses physical presentation units where practical: energy in eV, gate voltage in V, and steering angle in degrees.

1. Gate-tunable strong-to-weak coupling.
2. Gate-controlled complex reflection coefficient.
3. Inverse-designed gate voltage profile for target beam angles.
4. Electrically programmable far-field beam steering.
5. Amplitude-compensated phase modulation comparing one-layer and two-layer TMD designs.

## Reproduce Simulations

```powershell
python -m pip install -r requirements.txt
python scripts/make_figures.py --output-dir output/figures
pytest
```

## Boundary

The Python model is a coupled-oscillator plus array-factor design simulation. Parameters are chosen to make the proposed mechanism visible and defensible; they are not claimed as measured fits unless explicitly verified in [`docs/literature_notes.md`](docs/literature_notes.md).
