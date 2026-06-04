from scripts.make_figures import generate_all


def test_generate_all_smoke(tmp_path):
    output = tmp_path / "figures"
    generate_all(output, points=51)
    pngs = sorted(output.glob("*.png"))
    pdfs = sorted(output.glob("*.pdf"))
    assert len(pngs) == 5
    assert len(pdfs) == 5

