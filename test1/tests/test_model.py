import numpy as np

from model.array_factor import array_factor, metapixel_positions, steering_peak_angle
from model.coupled_oscillator import CoupledOscillatorParameters, complex_reflection
from model.gate_response import exciton_linewidth, gate_grid
from model.pipeline import run_pipeline
from model.reflection import phase_gradient_for_angle


def test_gate_response_shapes_and_monotonic_linewidth():
    gate = gate_grid(points=51)
    linewidth = exciton_linewidth(gate)
    assert gate.shape == linewidth.shape
    assert np.all(np.isfinite(linewidth))
    assert linewidth[-1] > linewidth[0]


def test_coupled_oscillator_reflection_is_complex_and_finite():
    energy = np.linspace(1.60, 1.90, 40)
    linewidth = np.linspace(0.018, 0.090, 40)
    response = complex_reflection(energy, linewidth, CoupledOscillatorParameters())
    assert response.shape == energy.shape
    assert np.iscomplexobj(response)
    assert np.all(np.isfinite(response.real))
    assert np.all(np.isfinite(response.imag))


def test_array_factor_peak_moves_with_phase_gradient():
    positions = metapixel_positions(count=96, spacing_m=0.32e-6)
    angles = np.linspace(-45, 45, 601)
    wavelength = 710e-9
    phases_0 = phase_gradient_for_angle(positions, wavelength, 0.0)
    phases_20 = phase_gradient_for_angle(positions, wavelength, 20.0)
    peak_0 = steering_peak_angle(angles, array_factor(positions, phases_0, wavelength, angles))
    peak_20 = steering_peak_angle(angles, array_factor(positions, phases_20, wavelength, angles))
    assert abs(peak_0) < 1.0
    assert 15.0 < peak_20 < 25.0


def test_pipeline_outputs_are_deterministic_and_complete():
    first = run_pipeline()
    second = run_pipeline()
    np.testing.assert_allclose(first.reflectance, second.reflectance)
    np.testing.assert_allclose(first.design_reflection, second.design_reflection)
    assert first.reflectance.shape == (first.params.energy_points, first.params.gate_points)
    assert set(first.far_field_intensity) == {0.0, 10.0, 20.0}
    assert all(np.all(np.isfinite(v)) for v in first.voltage_profiles_v.values())


def test_pipeline_steering_peaks_track_targets():
    result = run_pipeline()
    assert abs(result.far_field_peak_deg[0.0]) < 1.0
    assert abs(result.far_field_peak_deg[10.0] - 10.0) < 3.0
    assert abs(result.far_field_peak_deg[20.0] - 20.0) < 3.5


def test_design_energy_has_phase_amplitude_tradeoff():
    result = run_pipeline()
    energy_indices = [
        int(np.argmin(np.abs(result.energy_ev - energy)))
        for energy in (1.665, result.params.design_energy_ev, 1.725)
    ]
    phase_spans = []
    amplitude_spans = []
    for idx in energy_indices:
        response = result.reflection[idx, :]
        phase_spans.append(float(np.ptp(np.unwrap(np.angle(response)))))
        amplitude_spans.append(float(np.ptp(np.abs(response))))
    assert max(phase_spans) > 1.5
    assert max(amplitude_spans) > min(amplitude_spans)
