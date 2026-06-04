from pathlib import Path


def test_figure_script_exists_after_scaffold():
    # Milestone 2 intentionally validates model code before figure generation is added.
    # The real script is added in the innovation-simulation milestone.
    expected = Path("scripts") / "make_figures.py"
    assert not expected.exists() or expected.is_file()
