# Scalar Complex SHG Model

This folder contains a script-based phenomenological model for the proposed innovation:

> Gate-programmable zeros and phase winding of the scalar complex SHG field in exciton-polaron-mediated bilayer WSe2.

## Model Chain

1. `gate_coordinates.py`: converts dual-gate voltages into normalized carrier density and displacement coordinates.
2. `susceptibility.py`: builds layer-resolved complex Lorentz oscillator susceptibilities for neutral-exciton and exciton-polaron channels.
3. `shg_field.py`: computes the scalar coherent bilayer SHG field.
4. `topology.py`: locates near-zeros and computes phase winding along closed gate loops.
5. `heterodyne.py`: simulates reference-field interference.
6. `pipeline.py`: assembles the full gate-grid model.

## Run

From the repository root:

```bash
python scripts/make_figures.py --output-dir output/figures
pytest
```

The model is qualitative-to-semiquantitative. Parameters are chosen to be plausible and mechanism-revealing, but the output is not a fit to raw experimental data.

