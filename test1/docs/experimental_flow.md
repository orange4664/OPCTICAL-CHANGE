# Experimental Flow

## Goal

Design an electrically programmable excitonic metasurface that steers reflected light by tuning the complex reflection coefficient of each metapixel.

## Main Logic

The starting paper already shows that a monolayer MoSe2 excitonic metasurface can control reflected wavefronts. The limitation is that bare-exciton phase tuning can be tied to amplitude loss. This project transfers gate-tunable strong coupling from hybrid-2D excitonic metasurfaces into the beam-steering setting.

The intended physical chain is:

`Vg -> gamma_x(Vg) -> r(Vg)=|r|exp(i phi) -> phi_j=k0 x_j sin(theta0) -> far-field peak at theta0`

## Device Concept

Baseline structure:

- non-local dielectric metasurface
- hBN encapsulation
- monolayer MoSe2 or WS2
- transparent or patterned top gate
- bottom gate / substrate

Supporting extension:

- two-layer TMD stack such as WS2 / MoSe2 separated by hBN
- used to improve amplitude stability while retaining phase control

## Measurement Loop

1. Sweep photon energy and gate voltage to map reflection `R(E,Vg)`.
2. Fit the response with a coupled-oscillator model and extract `r(Vg)`.
3. Select target beam angles such as 0, 10, and 20 degrees.
4. Convert each target angle to a phase gradient and inverse-design a gate-voltage profile.
5. Measure the far-field reflection in a Fourier plane and check whether the main lobe reaches the target angle.

## What Python Checks Before the Experiment

Python does not replace the experiment. It checks whether the proposed design has a coherent control chain:

- gate tuning can visibly alter the strong-coupling reflection map
- a metapixel can sweep useful complex reflection phases
- a desired angle can be translated into a voltage profile
- the voltage-derived phase profile steers a far-field beam
- the two-layer TMD design can improve amplitude stability over a useful phase range

## Boundary

The simulations use representative, physically interpretable parameters. They are design simulations, not measured spectra and not COMSOL/FDTD full-wave calculations.
