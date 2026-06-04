# Visual Workflow Summary

Source PDF: `source/低维材料_图片合集.pdf`

The PDF is a four-page image workflow. It is used as the project flow reference, while the generated Python figures in `output/figures/` will be new simulations for the proposed design.

## Page 1: One-Slide Logic

The proposal follows:

1. Main paper A: MoSe2 excitonic beam steering in an active vdW metasurface.
2. Existing limitation: bare-exciton phase tuning can cause obvious amplitude loss.
3. New method B: gate-tunable strong coupling and amplitude-phase control in hybrid-2D excitonic metasurfaces.
4. Proposed experiment C: electrically controlled exciton-polariton phased array for programmable reflected beam steering.

Core upgrade:

`bare-exciton phased array -> gate-tunable exciton-polariton phased array`

## Page 2: Physical Mechanism

The mechanism chain is:

`gate voltage Vg -> carrier density / exciton linewidth -> complex reflection r(Vg)=|r|exp(i phi) -> array phase gradient -> far-field beam steering`

The key point is that voltage first changes each metapixel response, then multiple metapixels combine into a controllable far-field wavefront.

## Page 3: Experiment and Measurement Flow

The proposed sample is a reflection geometry:

- non-local dielectric metasurface
- hBN / monolayer MoSe2 or WS2 / hBN
- transparent top gate or patterned local gates
- bottom gate / substrate

The optical path is:

`tunable laser -> polarizer -> objective -> electrically addressable sample -> Fourier-plane imaging -> CCD/sCMOS`

The five-step loop is:

1. Sweep wavelength and gate voltage to measure reflection spectra.
2. Fit/extract complex reflection coefficients.
3. Choose target steering angle.
4. Inverse-design the voltage profile across metapixels.
5. Verify the far-field peak in the Fourier plane.

## Page 4: Python Simulation Outputs

The PDF asks for four core simulation panels:

1. Strong-coupling reflection spectrum versus energy and gate voltage.
2. Single-pixel complex reflection coefficient versus gate voltage.
3. Target-angle-dependent gate voltage profiles.
4. Far-field beam steering intensity.

This project also includes a fifth support panel. The earlier one-layer/two-layer hand-shaped compensation curve has been replaced by a coupled-oscillator-model phase-amplitude trade-off panel, so the figure now stays inside the same simulation chain as the first four panels.
