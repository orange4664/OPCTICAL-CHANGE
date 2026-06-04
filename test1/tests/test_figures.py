from scripts.make_figures import FIGURE_BASENAMES, generate_figures


def test_generate_all_required_figures(tmp_path):
    paths = generate_figures(tmp_path)
    expected_names = {
        f"{basename}{suffix}" for basename in FIGURE_BASENAMES for suffix in (".png", ".pdf")
    }
    assert {path.name for path in paths} == expected_names
    assert all(path.exists() and path.stat().st_size > 1000 for path in paths)
