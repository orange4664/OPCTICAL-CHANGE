# Literature Verification Notes

Task: `06-04-upgrade-docx-main-thesis`

Date: 2026-06-04

## Scope

This note verifies the minimum literature facts needed before building the Python model and drafting the main document. It is not a full literature review. The final document should use these facts to define the novelty boundary for one innovation point:

> Gate-programmable zeros and phase winding of the scalar complex SHG field in exciton-polaron-mediated bilayer WSe2.

## Verified / Usable Facts

### Baseline Paper: Cha et al. 2024

Reference:

- Soonyoung Cha, Tianyi Ouyang, Takashi Taniguchi, Kenji Watanabe, Nathaniel M. Gabor, and Chun Hung Lui, "Enhancing Resonant Second-Harmonic Generation in Bilayer WSe2 by Layer-Dependent Exciton-Polaron Effect," Nano Letters 24, 46, 14847-14853 (2024). DOI: `10.1021/acs.nanolett.4c04544`.
- Primary URLs:
  - https://pubs.acs.org/doi/10.1021/acs.nanolett.4c04544
  - https://arxiv.org/abs/2407.01854

Verified facts:

- The baseline platform is dual-gated bilayer WSe2.
- The mechanism is layer-dependent exciton-polaron formation: injected holes can be localized in one layer, inducing exciton-polaron states in that layer while the other layer remains closer to neutral-exciton behavior.
- The reported observable is resonant SHG intensity enhancement / quenching as a function of gate-controlled carrier state.
- The abstract reports about 40-fold SHG enhancement using a small electric field, described as about 3 percent of a critical breakdown-field comparison.
- The paper should be treated as an experimental SHG-control baseline with gate-coordinate / field analysis. It is not evidence that the original work used a named simulation package such as COMSOL, FDTD, or DFT as the central method.

Use in final document:

- Use Cha 2024 as the baseline paper and novelty boundary.
- Do not claim that our Python model reproduces Cha 2024 raw data.
- Do not present ordinary SHG enhancement / quenching as our innovation.

### Earlier Electrical SHG Control: Seyler et al. 2015

Reference:

- Kyle L. Seyler et al., "Electrical Control of Second-Harmonic Generation in a WSe2 Monolayer Transistor," Nature Nanotechnology 10, 407-411 (2015). DOI: `10.1038/nnano.2015.73`.
- Primary / institutional URLs:
  - https://arxiv.org/abs/1504.05247
  - https://www.ornl.gov/publication/electrical-control-second-harmonic-generation-wse2-monolayer-transistor

Verified facts:

- The work demonstrated electrical control of second-order optical nonlinearities in monolayer WSe2.
- The abstract reports SHG intensity at the A-exciton resonance tunable by more than an order of magnitude at low temperature and nearly a factor of 4 at room temperature through electrostatic doping.
- The mechanism is tied to exciton charging effects and oscillator-strength redistribution at exciton / trion resonances.

Use in final document:

- Use as evidence that "electrical control of SHG intensity" is not the new contribution here.
- Our novelty should be framed as scalar complex-field zero / phase-winding control, not generic SHG intensity tuning.

### SHG Field Interference and Phase: Kim et al. 2020

Reference:

- Wontaek Kim, Je Yhoung Ahn, Juseung Oh, Ji Hoon Shim, and Sunmin Ryu, "Second-Harmonic Young Interference in Atom-Thin Heterocrystals," Nano Letters 20, 8825 (2020). DOI: `10.1021/acs.nanolett.0c03763`.
- Primary URL:
  - https://arxiv.org/abs/2008.02403

Verified facts:

- The work directly showed SHG in TMD heterobilayers is governed by interference between two coherent second-harmonic fields.
- It used spectral phase interferometry to access material-dependent SH phase delays.
- It quantified frequency-dependent phase differences between MoS2 and WS2, with agreement against polarization-resolved data and first-principles calculations on complex susceptibility.

Use in final document:

- Use as precedent that SHG field phase and coherent layer interference are established physical observables.
- Our novelty should be active gate programming of a scalar complex SHG zero / winding in an exciton-polaron-mediated WSe2 setting, not merely the existence of SHG interference.

### MoTe2/WSe2 Destructive SHG Interference / Polarization Outlook: Wang et al. 2026 Preprint

Reference:

- Yiduo Wang et al., "Destructive interference of second harmonic generation in AA stacked MoTe2/WSe2," arXiv:2605.21231 (submitted May 20, 2026).
- Primary URL:
  - https://arxiv.org/abs/2605.21231

Verified facts from arXiv search / abstract metadata:

- This is a 2026 preprint, not yet treated here as a peer-reviewed settled baseline.
- It reports unconventional destructive SHG interference in nearly 0-degree / AA-stacked MoTe2/WSe2 heterobilayers.
- It attributes the effect to distinct two-photon resonances associated with WSe2 C exciton and MoTe2 D exciton, producing a near-pi phase difference in second-order susceptibility.
- It further discusses small-angle twisted MoTe2/WSe2, Poincare-sphere mapping, near-circular SHG output, abrupt azimuthal rotation, and geometric polarization singularity.

Use in final document:

- Use only as recent preprint / outlook context for destructive SHG interference and polarization-singularity extensions.
- Do not make polarization singularity a main claim of the WSe2 proposal.
- The main model should stay scalar: complex SHG field zero, phase jump, and winding.

### SHAARP Tooling Reference

Reference:

- Rui Zu et al., "Analytical and numerical modeling of optical second harmonic generation in anisotropic crystals using #SHAARP package," npj Computational Materials 8, 246 (2022). DOI: `10.1038/s41524-022-00930-4`.
- Primary URLs:
  - https://arxiv.org/abs/2208.03872
  - https://github.com/Rui-Zu/SHAARP

Verified facts:

- SHAARP stands for Second Harmonic Analysis of Anisotropic Rotational Polarimetry.
- It is an open-source package for analytical and numerical modeling of reflected optical SHG from a single interface.
- It supports arbitrary crystal symmetry / orientation, complex dielectric functions, and general polarization states.
- It is useful as a reference for SHG polarimetry / anisotropic-crystal modeling, but it is not required for this task.

Use in final document:

- Mention as optional methodological context only.
- Do not use SHAARP as a dependency for our scalar phenomenological model unless scope is reopened.

## Claim Boundary for This Project

The final document may state:

- The project proposes and numerically validates a gate-programmable scalar complex-SHG-field zero and phase-winding mechanism in bilayer WSe2.
- The Python model is a literature-constrained phenomenological model.
- The model provides reproducible theoretical validation / numerical certification of mechanism plausibility and measurable signatures.
- Experimental observation remains a proposed validation path.

The final document must not state:

- That the project has experimentally observed SHG zeros or phase winding.
- That the Python model fits Cha 2024 raw data.
- That Cha 2024 used COMSOL / FDTD / DFT as its central simulation method.
- That polarization singularity / Poincare-sphere behavior is the main WSe2 claim.

## Reference List Draft

[1] S. Cha, T. Ouyang, T. Taniguchi, K. Watanabe, N. M. Gabor, and C. H. Lui, "Enhancing Resonant Second-Harmonic Generation in Bilayer WSe2 by Layer-Dependent Exciton-Polaron Effect," Nano Letters 24, 14847-14853 (2024). DOI: 10.1021/acs.nanolett.4c04544.

[2] K. L. Seyler et al., "Electrical Control of Second-Harmonic Generation in a WSe2 Monolayer Transistor," Nature Nanotechnology 10, 407-411 (2015). DOI: 10.1038/nnano.2015.73.

[3] W. Kim, J. Y. Ahn, J. Oh, J. H. Shim, and S. Ryu, "Second-Harmonic Young Interference in Atom-Thin Heterocrystals," Nano Letters 20, 8825 (2020). DOI: 10.1021/acs.nanolett.0c03763.

[4] Y. Wang et al., "Destructive interference of second harmonic generation in AA stacked MoTe2/WSe2," arXiv:2605.21231 (2026).

[5] R. Zu et al., "Analytical and numerical modeling of optical second harmonic generation in anisotropic crystals using #SHAARP package," npj Computational Materials 8, 246 (2022). DOI: 10.1038/s41524-022-00930-4.

