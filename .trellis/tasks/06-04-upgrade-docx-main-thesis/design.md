# Upgrade Document to Main Thesis - Design

## Architecture and Boundaries

This task has two work surfaces:

- Document surface: transform the source `.docx` into a polished main-thesis / main-paper deliverable.
- Reproducibility surface: implement Python modeling scripts and generate figures that support the document's central claims.
- Repository surface: isolate this directory as its own Git repository and push only this task's files to `https://github.com/orange4664/OPCTICAL-CHANGE.git`.

The parent Git repository is out of scope except as an environmental risk. Work must not stage, commit, or push files from the parent `codex` repository.

## Document Design

Preserve the original source file and write edited output as a separate deliverable. The expected output location is `output/doc/` unless the user chooses a different final filename or format.

The document should be reorganized from a brainstorming draft into a focused Chinese main-thesis style narrative with selected English scientific framing. It is a refinement of one innovation point derived from the baseline paper, not a broad field review.

1. Central thesis and title.
2. Baseline paper and novelty boundary.
3. Literature gap: intensity control vs complex-field control.
4. Core physics claim: gate-programmable SHG zeros and phase winding.
5. Minimal reproducible model:
   - gate voltage to carrier density / displacement field;
   - layer-resolved complex Lorentz susceptibility;
   - coherent bilayer SHG field;
   - zero finding and winding number;
   - heterodyne SHG observable.
6. Proposed figures and experimental validation.
7. Controls and reviewer-risk responses.
8. Final claim statement and limitations.
9. `模型边界与可验证性` if a separate final section reads better than folding limitations into section 8.

Target depth:

- 12-18 pages.
- 6-8 main sections.
- No appendix by default.
- Background literature is included only to establish the novelty boundary for the single innovation point.

Required boundary statements:

- No fit to Cha 2024 raw experimental data.
- No claim of completed experimental observation for SHG zeros / winding.
- No DFT / COMSOL / FDTD simulation in this scope.
- No polarization singularity main claim.

One-sentence innovation anchor:

- Chinese: `双栅调控 exciton-polaron 共振，实现双层 WSe2 标量复 SHG 场的电控零点与相位绕转。`
- English: `Gate-programmable zeros and phase winding of the scalar complex SHG field in exciton-polaron-mediated bilayer WSe2.`

Main-claim boundary:

- Mainline: scalar complex SHG field, SHG zeros, phase jump, phase winding, and heterodyne observables.
- Outlook only: polarization singularity, Jones / Stokes vector analysis, and Poincare sphere trajectories, especially for twisted heterobilayer extensions.

Language contract:

- Body text: primarily Chinese.
- Title: Chinese title plus English title.
- Abstract / central claim: Chinese version plus concise English version.
- Technical terms: preserve key English phrases such as `complex second-harmonic field`, `gate-programmable zero`, `phase winding`, `exciton-polaron`, and `heterodyne SHG` where they improve precision.

Reference contract:

- Use simple numbered in-text citations, for example `[1]`.
- Add a formal numbered reference section at the end of the document.
- Do not use Zotero, Word citation fields, or another citation manager unless the user reopens this decision.
- Keep each reference human-readable with enough metadata to identify the source.

## Data Flow and Contracts

- Input: `我会把它升级成主论_2026-06-04-11-49-07.docx`.
- Intermediate planning: `.trellis/tasks/06-04-upgrade-docx-main-thesis/`.
- Code / figure output: a clearly named reproducibility folder and stable generated-figure folder.
- Final document: a named `.docx` output that does not overwrite the source unless explicitly requested.
- Primary final document filename: `output/doc/双栅WSe2复SHG零点与相位绕转_主论稿.docx`.
- ASCII-friendly companion / README reference: `output/doc/wse2_complex_shg_zero_phase_winding_main.docx`.

The edited document must not contain fabricated data, placeholder citations, or unsupported claims. If literature verification is requested, claims about publication year, title, authors, and reported findings must be checked before final wording.

Execution order contract:

- Verify literature / claim boundaries first.
- Build Python model and figures second.
- Draft the Word document after the model figures exist, so the document is evidence-led rather than figure-fitted after the fact.

Literature verification should rely on primary sources where possible:

- journal pages, preprints, or official abstracts for cited scientific papers;
- official GitHub / documentation pages for software tools;
- no unsupported claims from the source draft should be promoted into final conclusions.

## Reproducibility Design

Use Python as the executable modeling target. MATLAB can be referenced conceptually in the document, but Python is the implementation deliverable unless the user later asks for MATLAB too.

The model is not a claim to reproduce a named simulation package from the baseline Cha 2024 paper. It is a phenomenological proposal model built on the experimental paper's gate-tuned SHG setting, intended to test whether complex SHG zeros, phase jumps, winding, and heterodyne observables are internally consistent and visually reproducible.

Selected model positioning: qualitative-to-semiquantitative. Use literature-constrained parameters where available, but label the output as a phenomenological mechanism model rather than a fit to Cha 2024 data.

Evidence posture:

- Python simulation can serve as this document's core evidence.
- Use wording such as `numerical validation`, `model-predicted signatures`, and `reproducible theoretical validation`.
- Experimental realization remains a proposed / expected validation path, not a completed result.

Feasibility constraints:

- Include lightweight filters for gate / displacement-field bounds, detectable SHG intensity along proposed paths, and literature-plausible linewidth / oscillator-strength ranges.
- Use these constraints to avoid figures that depend on extreme or unphysical parameters.
- Do not implement a full experimental optimizer or detailed device-design workflow.

Recommended modules:

- `gate_coordinates.py`: convert top / bottom gate voltages into carrier density and displacement-field-like coordinates.
- `susceptibility.py`: compute layer-resolved complex Lorentz oscillator susceptibilities.
- `shg_field.py`: compute coherent bilayer SHG fields, intensity, phase, real part, and imaginary part.
- `topology.py`: find zeros and compute phase winding along gate loops.
- `heterodyne.py`: simulate reference-field interference and phase retrieval observables.
- `make_figures.py`: generate all key figures from one command.

Packaging contract:

- Use a script-based minimal package rather than notebook-first analysis.
- Include a modeling `README.md` with setup, execution command, figure descriptions, and limitations.
- Include a root `README.md` that links final document output, model README, generated figures, reproduction command, and boundary statements.
- Provide one stable command to regenerate the figure set.
- Use `requirements.txt` with `numpy`, `matplotlib`, `scipy`, and `pytest`.
- Add focused tests for gate-coordinate conversion, susceptibility / SHG field shape behavior, winding-number behavior on a known loop, and figure-generation smoke behavior.

Generated figures should cover:

- innovation setup / model-coordinate schematic rather than a reproduction of Cha 2024 figures;
- complex field maps for intensity, phase, real part, and imaginary part;
- complex-plane gate-path trajectory with phase jump / winding;
- winding-number or loop diagnostic map;
- heterodyne fringe simulation;
- parameter robustness / literature-constrained sweep where useful.

Figure packaging should prefer multi-panel main figures, for example:

- Figure 1: innovation setup and model coordinates, combining device / gate-coordinate schematic, layer-selective exciton-polaron cartoon, coherent SHG field sum, and the new complex-field observables.
- Figure 2: complex-field map with `|E|^2`, `arg(E)`, `Re(E)`, and `Im(E)` panels.
- Figure 3: path analysis combining gate path, complex-plane trajectory, intensity along path, and unwrapped phase.
- Figure 4: loop / winding diagnostic plus robustness panels.
- Figure 5: heterodyne observable panels.

Jones vector / Stokes parameter / Poincare sphere figures are not required for the main deliverable.

## GitHub Upload Design

Implementation should:

- initialize a nested Git repository in `OPCTICAL-CHANGE` if `.git` is absent;
- set `origin` to `https://github.com/orange4664/OPCTICAL-CHANGE.git`;
- commit only files inside `OPCTICAL-CHANGE`;
- include this task's Trellis planning files in baseline commits;
- exclude `.trellis/workspace`, unrelated tasks, temporary files, and render artifacts via `.gitignore` / selective staging;
- push after meaningful milestones according to the selected cadence.

Milestone-based push is preferred over clock-based background automation because it avoids committing half-written files and does not require a long-running watcher.

Selected push milestones:

- repository setup / baseline capture;
- literature verification complete;
- Python model and generated figures complete;
- Word initial full draft complete;
- final visual QA / polished delivery.

## Compatibility and Rollback

- Original `.docx` stays available as rollback baseline.
- If Word rendering tools are unavailable, extract text and report layout risk, then ask for local visual review or install the missing render dependency with approval.
- If GitHub push fails due to auth or remote mismatch, do not change parent Git settings; stop and report the exact failure.

## Open Trade-offs

- Implementation approval after planning review.
