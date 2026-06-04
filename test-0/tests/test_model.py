import numpy as np

from model.gate_coordinates import gate_to_density_displacement, layer_density_split
from model.pipeline import run_model
from model.shg_field import normalize_intensity
from model.topology import phase_winding


def test_gate_coordinate_shapes():
    vt, vb = np.meshgrid(np.linspace(-1, 1, 5), np.linspace(-1, 1, 5))
    density, displacement = gate_to_density_displacement(vt, vb)
    assert density.shape == vt.shape
    assert displacement.shape == vt.shape
    assert np.isclose(density[2, 2], 0.0)
    assert np.isclose(displacement[2, 2], 0.0)


def test_layer_density_split_conserves_positive_density():
    density = np.array([0.0, 1.0, 2.0])
    displacement = np.array([-2.0, 0.0, 2.0])
    top, bottom, polarization = layer_density_split(density, displacement)
    np.testing.assert_allclose(top + bottom, density)
    assert np.all(np.abs(polarization) <= 1.0)


def test_pipeline_outputs_complex_field():
    result = run_model(points=41)
    assert result.field.shape == (41, 41)
    assert np.iscomplexobj(result.field)
    assert result.relative_intensity.shape == result.field.shape
    assert np.nanmax(result.relative_intensity) <= 1.0 + 1e-12


def test_phase_winding_known_circle():
    theta = np.linspace(0, 2 * np.pi, 200)
    values = np.exp(1j * theta)
    assert np.isclose(phase_winding(values), 1.0, atol=1e-6)


def test_normalize_intensity_handles_zero():
    data = np.zeros((3, 3))
    out = normalize_intensity(data)
    assert np.all(out == 0.0)

