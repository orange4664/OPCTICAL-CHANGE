# Literature Notes

This file verifies the short list of literature claims used by the README and PPT-ready outline. It is not a full literature review.

## Main Paper A

**Melissa Li, Claudio U. Hail, Souvik Biswas, Harry A. Atwater, "Excitonic Beam Steering in an Active van der Waals Metasurface."**

- Status: published journal article.
- Venue: *Nano Letters* 23(7), 2023.
- DOI: <https://doi.org/10.1021/acs.nanolett.3c00032>
- Verification sources:
  - ACS article page: <https://pubs.acs.org/doi/10.1021/acs.nanolett.3c00032>
  - OSTI journal record: <https://www.osti.gov/biblio/2419205>
  - arXiv preprint: <https://arxiv.org/abs/2211.09297>
- Verified points used here:
  - The system is an active van der Waals metasurface based on monolayer MoSe2 excitonic resonances.
  - It dynamically controls reflection amplitude and phase profiles.
  - It demonstrates reflected beam steering between about -30 deg and +30 deg near excitonic resonances. The published ACS abstract names A and B excitons; the arXiv abstract/source-document wording also mentions a trion resonance.
- Wording caution:
  - This is the starting point, not our claimed new result. Our proposal changes the control mechanism from bare excitons to gate-tunable exciton-polariton / strong-coupling control.

## New Method B1: Electrically Tunable Strong Coupling

**Tom Hoekstra, Jorik van de Groep, "Electrically tunable strong coupling in a hybrid-2D excitonic metasurface for optical modulation."**

- Status: arXiv preprint in 2025; formally published in 2026.
- Venue: *Light: Science & Applications* 15, 28 (2026).
- DOI: <https://doi.org/10.1038/s41377-025-02079-3>
- Verification sources:
  - Journal version: <https://www.nature.com/articles/s41377-025-02079-3>
  - arXiv preprint: <https://arxiv.org/abs/2502.12132>
- Verified points used here:
  - The work combines a gate-tunable 2D semiconductor heterostructure with a non-local dielectric metasurface.
  - It achieves strong and electrically tunable exciton-photon coupling at ambient conditions.
  - The gate response is described as a continuous strong-to-weak coupling transition mediated by carrier-density-induced changes in the exciton nonradiative decay rate.
  - It experimentally demonstrates 9.9 dB reflectance modulation.
- Wording caution:
  - In project docs, call this a 2026 published paper, with a 2025 arXiv/preprint history if needed.
  - The 9.9 dB value is verified for their optical modulation device; in our project it motivates the mechanism and is not claimed for the proposed beam-steering design.

## Supporting Method B2: Complex Amplitude Control

**Tom Hoekstra, Mark L. Brongersma, Jorik van de Groep, "Hybrid-2D Excitonic Metasurfaces for Complex Amplitude Modulation."**

- Status: published journal article.
- Venue: *Nano Letters* 26(18), 2026.
- DOI: <https://doi.org/10.1021/acs.nanolett.6c00072>
- Verification sources:
  - ACS article page: <https://pubs.acs.org/doi/10.1021/acs.nanolett.6c00072>
  - arXiv preprint: <https://arxiv.org/abs/2604.07619>
- Verified points used here:
  - The work numerically demonstrates a hybrid-2D excitonic metasurface platform for independent amplitude and phase control in the visible regime.
  - It uses gate-tunable excitonic response of monolayer WS2 retrieved from experiments.
  - Adding a second tunable monolayer enables independent amplitude and phase control over the full 0-2pi phase range.
  - It applies the platform to a reconfigurable beam-steering metadevice.
- Wording caution:
  - This is supporting evidence for the one-layer vs two-layer TMD amplitude-stability panel. It should not replace the core innovation: electrically controlled strong-coupling beam steering.

## Project Wording Rules

- It is accurate to say the proposal transfers electrically tunable strong coupling into the excitonic beam-steering setting.
- It is accurate to use the two-layer TMD result as supporting evidence for more stable amplitude-phase control.
- Do not claim that our Python output is experimental data.
- Do not claim that the proposed design has demonstrated 9.9 dB modulation or 88.5% steering efficiency; those numbers belong to the cited works and should remain context-specific.
