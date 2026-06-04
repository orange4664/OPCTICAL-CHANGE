# Upgrade document to main thesis

## Goal

Upgrade the existing Word draft into a main-thesis / main-paper style deliverable centered on a PRL-level, testable nonlinear optics proposal, while keeping the work reproducible and periodically backed up to the requested GitHub repository.

Source document:

- `我会把它升级成主论_2026-06-04-11-49-07.docx`

Requested GitHub repository:

- `https://github.com/orange4664/OPCTICAL-CHANGE.git`

## Confirmed Facts

- The source `.docx` is present in the `OPCTICAL-CHANGE` directory.
- The document currently reads like a proposal / concept draft rather than a finished main thesis or main paper.
- Extracted DOCX structure:
  - 335 non-empty paragraphs.
  - 1 table.
  - Microsoft Word metadata reports 4 pages, but the extracted paragraph count is much larger, so visual rendering must be verified during implementation.
  - No substantive comments or footnotes were found.
- The scientific topic is:
  - Cha 2024 dual-gated bilayer WSe2 resonant SHG as the baseline paper.
  - Proposed upgrade path: gate-programmable complex chi(2), SHG zeros, phase jumps / phase winding, and phase-resolved heterodyne SHG validation.
  - Reproducibility requirement: Python / MATLAB style modeling using gate-coordinate conversion, complex Lorentz oscillator susceptibility, coherent layer SHG summation, zero finding, winding number analysis, and heterodyne fringe simulation.
- The baseline Cha 2024 paper appears to be an experimental paper with gate-coordinate / field analysis rather than a COMSOL, FDTD, DFT, or named simulation-software paper. The Python deliverable should therefore be framed as a new phenomenological reproducibility model for this proposal, not as a reproduction of the original paper's hidden simulation software.
- User selected the model positioning: qualitative-to-semiquantitative, specifically a literature-constrained phenomenological model. Parameters should be kept within literature-plausible ranges where possible, but the work must not claim a fit or reproduction of Cha 2024 experimental data unless such a fit is actually performed.
- User selected the main-claim boundary: keep the central claim on scalar complex SHG zeros and phase winding. Polarization singularity / Poincare sphere content belongs only in outlook or optional appendix material, not in the main claim or required figure set.
- User selected the reference strategy: maintain a formal numbered reference list in the document and use simple in-text numeric citations such as `[1]`, without introducing a citation manager or Word citation fields.
- User selected the Python deliverable shape: script-based minimal package plus `README.md`, with one clean command to regenerate figures; no notebook in the first version.
- User selected a lightly engineered Python dependency / test strategy: use `numpy`, `matplotlib`, `scipy`, and `pytest`, with focused tests for core numerical functions and figure-generation smoke behavior.
- User selected the document depth: 12-18 pages, no appendix by default, and 6-8 main sections. This is a focused refinement of one innovation point derived from the baseline paper, not a broad review or full thesis.
- User selected the one-sentence innovation name:
  - Chinese: `双栅调控 exciton-polaron 共振，实现双层 WSe2 标量复 SHG 场的电控零点与相位绕转。`
  - English: `Gate-programmable zeros and phase winding of the scalar complex SHG field in exciton-polaron-mediated bilayer WSe2.`
- User selected a multi-panel figure strategy: use a moderate number of main figures, but combine related plots into multi-panel figures to keep the 12-18 page document compact while preserving enough modeling evidence.
- User clarified the evidence posture: Python simulation / numerical validation is allowed as the core evidence for this document, but experimental realization must still be described as proposed or expected rather than already observed.
- User selected the experimental-feasibility modeling boundary: include lightweight experimental constraints in the Python model, but do not build a full experimental optimizer.
- User selected an explicit limitation / scope section, preferably titled `模型边界与可验证性`, to state what the work does not claim or implement.
- User selected baseline GitHub contents: include this task's Trellis planning files, but exclude `.trellis/workspace`, unrelated tasks, temporary files, and render artifacts.
- User selected final document naming: primary Chinese filename `output/doc/双栅WSe2复SHG零点与相位绕转_主论稿.docx`, with an ASCII-friendly companion or README reference `output/doc/wse2_complex_shg_zero_phase_winding_main.docx` where useful for scripts / GitHub references.
- User selected README deliverables: root `README.md` for project navigation and model-specific README for setup, execution, figure meanings, and model boundaries.
- User selected evidence-first implementation order: literature verification, then Python model / figures, then Word main document.
- The source draft already contains candidate title, innovation claims, model modules, figure plan, controls, reviewer objections, and final Chinese / English claim statements.
- User selected the full recommended deliverable scope: polished Word main-thesis / main-paper document plus reproducible Python modeling scripts and key generated figures.
- User selected the recommended language / format target: Chinese main-thesis style document with English title, English abstract / core claim, and Chinese-English technical terminology where useful.
- User selected necessary literature / scientific-fact verification before final writing. Key claims about cited papers, reported observations, and tools must be checked before final wording.
- User selected milestone-based GitHub uploads rather than clock-based background uploads.
- Current Git state is risky for direct push:
  - `git rev-parse --show-toplevel` reports the actual Git root as the parent `D:/桌面/aaaaa同济/同济杂七杂八/codex`, not the `OPCTICAL-CHANGE` directory.
  - Current `origin` is `https://github.com/orange4664/muon-benchmark.git`, not the requested `OPCTICAL-CHANGE.git`.
  - The parent Git worktree has many unrelated uncommitted changes outside this task.
- User approved the safe GitHub strategy: initialize `OPCTICAL-CHANGE` as an independent Git repository and set its `origin` to `https://github.com/orange4664/OPCTICAL-CHANGE.git`, instead of pushing from the parent Git root.

## Requirements

### Delivery Flow

This task should be implemented step by step. Each phase must leave a recoverable artifact before moving to the next phase.

#### Phase A - Repository Safety and Baseline

Input:

- Current `OPCTICAL-CHANGE` directory.
- Source `.docx`.
- Trellis planning files.

Output:

- Independent Git repository initialized inside `OPCTICAL-CHANGE`.
- `origin` set to `https://github.com/orange4664/OPCTICAL-CHANGE.git`.
- Baseline commit and push containing source document, this task's planning artifacts, and repository hygiene files such as `.gitignore`.

Gate:

- `git status --short` is clean or contains only expected post-baseline changes.
- `git remote -v` points to the requested repository.
- No parent-repo files are staged or pushed.
- `.trellis/workspace`, unrelated tasks, temporary files, and render artifacts are excluded.

#### Phase B - Literature and Fact Verification

Input:

- Source draft claims.
- Baseline paper and cited precedent papers / tools.

Output:

- A concise verification note under the task directory or output folder.
- Corrected claim boundaries for the final document.

Gate:

- Key statements about Cha 2024, SHG phase interferometry precedent, MoTe2/WSe2 destructive interference / polarization precedent, and SHAARP tooling are either verified, softened, or removed.
- Unsupported source-draft claims are not promoted into final conclusions.
- Milestone commit and push completed.

#### Phase C - Reproducible Python Model

Input:

- Verified scientific framing.
- Literature-plausible parameter ranges where available.

Output:

- Python scripts for gate coordinates, complex susceptibility, coherent SHG field, zero / winding analysis, and heterodyne simulation.
- A documented command that regenerates all key figures.

Gate:

- The code runs from a clean command.
- The generated figures demonstrate the intended mechanism chain:
  - innovation setup / model-coordinate schematic;
  - complex field maps;
  - zero / phase jump or winding trajectory;
  - heterodyne observable.
- The model is labeled as a literature-constrained phenomenological model, not a fit to Cha 2024 data.
- Milestone commit and push completed.

#### Phase D - Main Document Draft

Input:

- Source `.docx`.
- Verified claim notes.
- Generated Python figures.

Output:

- Separate edited `.docx` output, not overwriting the source.
- Chinese main-thesis style body with English title, concise English abstract / claim, and key bilingual terms.
- Target 12-18 pages, no appendix by default, and 6-8 main sections.
- Primary output filename: `output/doc/双栅WSe2复SHG零点与相位绕转_主论稿.docx`.
- ASCII-friendly filename / reference where useful: `output/doc/wse2_complex_shg_zero_phase_winding_main.docx`.

Gate:

- The document has a clear section hierarchy:
  - central claim;
  - baseline and novelty boundary;
  - literature gap;
  - model and generated figures;
  - proposed experiment and controls;
  - limitations / reviewer-risk handling.
- Figures and text tell the same mechanism story.
- Milestone commit and push completed.

#### Phase E - Visual QA and Final Delivery

Input:

- Draft `.docx`.
- Generated figures and scripts.

Output:

- Final `.docx` and reproducibility package.
- Final verification notes.

Gate:

- The document is rendered and visually checked if tools are available.
- If rendering tools are missing, the missing dependency and residual layout risk are reported.
- Final code regeneration command still works.
- Final milestone commit and push completed.

### Product Requirements

- Preserve the source document as a recoverable baseline or create an explicitly named edited output copy before major rewriting.
- Transform the draft into a coherent main-thesis / main-paper deliverable with:
  - a clear central claim;
  - a literature baseline and novelty boundary;
  - a main narrative organized around complex SHG field control rather than simple intensity enhancement;
  - testable theoretical and experimental criteria;
  - reproducible Python / MATLAB modeling plan and, if in scope, generated code / figures;
  - reviewer-risk handling and controls.
- Keep the central scientific claim focused on gate-programmable SHG zeros and phase winding of the scalar complex SHG field.
- Use the selected one-sentence innovation name as the repeated anchor for the document, model README, and figure narrative.
- Keep background and literature discussion scoped to the single innovation point. Do not expand into a broad SHG / TMD review unless needed to define novelty.
- Treat polarization singularity / Poincare sphere analysis as outlook-only unless the scope is explicitly reopened later.
- Include a `模型边界与可验证性` section that states:
  - no fit to Cha 2024 raw experimental data;
  - no claim of completed experimental observation for SHG zeros / winding;
  - no DFT / COMSOL / FDTD simulation in this scope;
  - no polarization singularity main claim.
- Write the final document primarily in Chinese, while preserving English scientific framing for the title, abstract / core claim, figure captions where useful, and key technical terms.
- Implement a reproducible Python modeling package / script set that demonstrates:
  - gate-coordinate conversion;
  - layer-resolved complex susceptibility;
  - coherent bilayer SHG field summation;
  - SHG zero finding;
  - phase jump / winding-number analysis;
  - heterodyne SHG fringe simulation.
- Provide a README for the modeling package that explains setup, one-command figure regeneration, figure meanings, and model limitations.
- Provide a root `README.md` that links the final document, model README, figure outputs, reproduction command, and core boundary statements.
- Do not create a notebook unless the scope is explicitly reopened.
- Provide `requirements.txt` for Python dependencies.
- Add focused tests for core model behavior and the figure-generation entry point; avoid heavy framework or broad test scaffolding.
- Generate key figures from the reproducible model and keep them in a stable output folder suitable for inserting into the Word document.
- Prefer multi-panel figures over many separate single-panel figures. Each generated figure should have a clear role in the mechanism chain and document narrative.
- State the modeling limitation clearly: the Python model demonstrates mechanism plausibility and observable criteria, not a unique quantitative extraction of material parameters.
- Treat Python modeling as reproducible theoretical validation / numerical certification of the proposed mechanism. Do not imply that SHG zeros or phase winding have already been experimentally observed in this work.
- Include lightweight feasibility filters in the model, such as reasonable gate / displacement-field bounds, detectable intensity along proposed paths, and literature-plausible linewidth / oscillator-strength ranges.
- Do not turn the project into a full experimental optimization or device-design task.
- Avoid overstating already-published results as this work's innovation.
- Verify key literature facts before finalizing scientific claims, especially the baseline Cha 2024 work, SHG phase-interferometry precedent, MoTe2/WSe2 destructive-interference / polarization-singularity precedent, and SHAARP tooling reference.
- Add a formal numbered reference section to the final document. Use simple in-text numeric citations and keep citation metadata human-readable.
- Validate the Word document visually before final delivery when the editing phase starts.
- Keep task planning, progress notes, and deliverables separated from unrelated parent-repo changes.
- Configure a GitHub backup / push workflow that targets `https://github.com/orange4664/OPCTICAL-CHANGE.git` without accidentally pushing unrelated files from the parent Git repository.
- Use an independent `.git` repository rooted at `OPCTICAL-CHANGE` for this work once implementation starts.
- Commit only this task's Trellis planning files, not the whole Trellis workspace or unrelated tasks.
- Commit and push at meaningful milestones:
  - repository setup / baseline capture;
  - literature verification complete;
  - Python model and generated figures complete;
  - Word initial full draft complete;
  - final visual QA / polished delivery.

## Acceptance Criteria

- [ ] PRD captures source-document facts, goal, scope boundaries, acceptance criteria, and unresolved user decisions.
- [ ] Complex-task planning includes `design.md` and `implement.md` before implementation starts.
- [x] A safe GitHub upload strategy is selected before any push attempt.
- [ ] Phase A repository baseline is completed and pushed.
- [ ] Baseline push includes this task's planning files and excludes Trellis workspace / unrelated tasks / temporary artifacts.
- [ ] Phase B literature / fact verification is completed and pushed.
- [ ] Phase C reproducible Python model and figures are completed and pushed.
- [ ] Phase D Word main-document draft is completed and pushed.
- [ ] Phase E visual QA / final delivery is completed and pushed.
- [ ] The final document has a clear title, thesis, section hierarchy, scientific novelty boundary, model / figure plan, and validation criteria.
- [ ] The final document stays within the selected 12-18 page / 6-8 main-section target unless the user approves expansion.
- [ ] The final document keeps polarization singularity / Poincare sphere material out of the main claim.
- [ ] The final document includes a concise `模型边界与可验证性` section.
- [ ] Reproducible Python code runs from a documented entry point and regenerates the key figures.
- [ ] The Python model is delivered as a script-based package with README documentation, not as notebook-only analysis.
- [ ] Root README and model README explain how the document, code, figures, and boundaries fit together.
- [ ] Python dependencies are documented in `requirements.txt`, and focused tests can be run with `pytest`.
- [ ] Generated figures align with the document narrative and are saved in a stable output folder.
- [ ] The Python model includes lightweight feasibility constraints and does not rely only on extreme or unphysical parameter choices.
- [ ] Key cited literature facts are verified and unsupported source-draft claims are corrected, softened, or removed.
- [ ] The final document contains a formal numbered reference list with human-readable citation metadata.
- [ ] Milestone commits and pushes are used for GitHub backup, without adding temporary render files or unrelated parent-repo changes.
- [ ] The final deliverable preserves or clearly separates the original source file from edited output.
- [ ] Final Word output uses the selected filename convention.
- [ ] Visual document review is performed or any missing rendering dependency / layout risk is explicitly reported.
- [ ] No unrelated parent-repo changes are committed or pushed as part of this task.

## Out of Scope

- Claiming guaranteed PRL acceptance.
- Making polarization singularity / Poincare sphere analysis a main claim for the WSe2 proposal.
- Building a full experimental optimizer or device-design tool.
- Fabricating citations, data, experimental results, or literature facts not supported by the source draft or later verified evidence.
- Pushing unrelated files from the parent `codex` Git repository.
- Reverting unrelated existing changes in the parent worktree.

## Open Questions

- User approval to start implementation after reviewing this planning set.

## Notes

- Keep `prd.md` focused on requirements, constraints, and acceptance criteria.
- Lightweight tasks can remain PRD-only.
- For complex tasks, add `design.md` for technical design and `implement.md` for execution planning before `task.py start`.
