# OPCTICAL-CHANGE

Focused thesis-proposal upgrade for one innovation point derived from Cha et al. 2024:

> Gate-programmable zeros and phase winding of the scalar complex SHG field in exciton-polaron-mediated bilayer WSe2.

This project directory is stored under `test-0/` in the repository root.

## Deliverables

- Source draft: `我会把它升级成主论_2026-06-04-11-49-07.docx`
- Source paper and original innovation note folder: `源论文和创新意见/`
- Planned final document: `output/doc/双栅WSe2复SHG零点与相位绕转_主论稿.docx`
- ASCII-friendly document reference: `output/doc/wse2_complex_shg_zero_phase_winding_main.docx`
- LaTeX source: `output/latex/wse2_complex_shg_zero_phase_winding_main.tex`
- LaTeX PDF: `output/latex/wse2_complex_shg_zero_phase_winding_latexpdf.pdf`
- Python model: `model/`
- Figure generation entry point: `scripts/make_figures.py`
- Generated figures: `output/figures/`

## Reproduce Figures

```bash
python -m pip install -r requirements.txt
python scripts/make_figures.py --output-dir output/figures
pytest
```

## Boundary

This project is a literature-constrained phenomenological model and main-document draft. It does not fit Cha 2024 raw data, does not claim completed experimental observation of SHG zeros / phase winding, and does not use DFT, COMSOL, or FDTD. Polarization singularity / Poincare-sphere analysis is treated only as an outlook.
