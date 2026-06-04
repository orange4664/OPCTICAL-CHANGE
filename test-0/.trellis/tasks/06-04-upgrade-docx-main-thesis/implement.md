# Upgrade Document to Main Thesis - Implementation Plan

## Checklist

1. Resolve remaining planning decisions:
   - none currently open.
2. Ask user to review planning artifacts and approve implementation.
3. Start Trellis task with `task.py start`.
4. Load pre-development guidance with `trellis-before-dev`.
5. Initialize isolated Git repository in `OPCTICAL-CHANGE` and set `origin` to `https://github.com/orange4664/OPCTICAL-CHANGE.git`.
6. Make an initial safety commit containing the source document, this task's planning files, and repository hygiene files, then push.
   - Exclude `.trellis/workspace`, unrelated tasks, temporary files, and render artifacts.
7. Prepare document-editing environment:
   - prefer `python-docx` for structured editing;
   - use DOCX rendering if available for visual checks;
   - keep intermediate renders in `tmp/docs/`.
8. Verify key literature and tool facts from primary sources where possible.
9. Create reproducible Python model scripts and generated figures in a stable output folder.
   - Use a script-based minimal package plus README.
   - Do not create a notebook unless the scope is reopened.
   - Add `requirements.txt` for `numpy`, `matplotlib`, `scipy`, and `pytest`.
   - Add focused pytest coverage for model primitives and figure-generation smoke behavior.
   - Include lightweight feasibility filters, but do not build a full experimental optimizer.
10. Add root `README.md` and model README.
11. Draft the upgraded document as a separate output `.docx`.
   - Target 12-18 pages and 6-8 main sections.
   - Keep the narrative focused on one innovation point derived from the baseline paper.
   - Keep background literature scoped to novelty framing, not broad review.
   - Include a concise `模型边界与可验证性` section.
   - Use `output/doc/双栅WSe2复SHG零点与相位绕转_主论稿.docx` as the primary output filename and keep an ASCII-friendly companion / reference where useful.
12. Render and inspect the final `.docx`; fix layout defects.
13. Commit and push at the selected milestones:
   - repository setup / baseline capture;
   - literature verification complete;
   - Python model and generated figures complete;
   - Word initial full draft complete;
   - final visual QA / polished delivery.
14. Run final Trellis quality check and wrap up.

## Validation Commands

- `git status --short`
- `git remote -v`
- `python -c "import docx; print('python-docx available')"` or equivalent dependency check
- DOCX render command if dependencies are available
- Reproducibility script execution if code / figures are in scope
- Figure regeneration command from a clean run directory
- `pytest`

## Risky Files and Rollback Points

- Source `.docx`: do not overwrite without explicit user approval.
- `.git/config`: configure only inside `OPCTICAL-CHANGE`, not the parent repository.
- Generated output folders: keep names stable and avoid mixing temporary render artifacts with final deliverables.

## GitHub Push Cadence

Default recommendation: commit and push after each meaningful milestone:

- repository setup / baseline capture;
- literature verification complete;
- Python model and generated figures complete;
- Word initial full draft complete;
- final visual QA / polished delivery.

Clock-based automatic pushing is out of scope unless the user later explicitly asks for it.
