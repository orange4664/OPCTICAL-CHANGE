"""Deterministic simulation pipeline for the beam-steering proposal."""

from __future__ import annotations

from dataclasses import dataclass, field

import numpy as np

from .array_factor import array_factor, metapixel_positions, steering_peak_angle
from .coupled_oscillator import (
    CoupledOscillatorParameters,
    complex_reflection,
    polariton_energies,
    reflection_map,
)
from .gate_response import exciton_linewidth, gate_grid
from .reflection import (
    amplitude,
    inverse_gate_for_phase,
    normalize_phase,
    phase,
    phase_gradient_for_angle,
    unwrap_phase,
)


@dataclass(frozen=True)
class SimulationParameters:
    energy_min_ev: float = 1.55
    energy_max_ev: float = 1.95
    energy_points: int = 260
    gate_min_v: float = -3.0
    gate_max_v: float = 3.0
    gate_points: int = 241
    design_energy_ev: float = 1.695
    wavelength_m: float = 710e-9
    metapixel_count: int = 96
    metapixel_spacing_m: float = 0.32e-6
    target_angles_deg: tuple[float, ...] = (0.0, 10.0, 20.0)
    scan_angles_deg: tuple[float, float, int] = (-60.0, 60.0, 801)
    oscillator: CoupledOscillatorParameters = field(default_factory=CoupledOscillatorParameters)


@dataclass(frozen=True)
class BeamSteeringResult:
    params: SimulationParameters
    energy_ev: np.ndarray
    gate_voltage_v: np.ndarray
    linewidth_ev: np.ndarray
    reflection: np.ndarray
    reflectance: np.ndarray
    design_reflection: np.ndarray
    design_amplitude: np.ndarray
    design_phase_rad: np.ndarray
    positions_m: np.ndarray
    target_angles_deg: np.ndarray
    voltage_profiles_v: dict[float, np.ndarray]
    phase_profiles_rad: dict[float, np.ndarray]
    far_field_angles_deg: np.ndarray
    far_field_intensity: dict[float, np.ndarray]
    far_field_peak_deg: dict[float, float]
    polariton_energies_ev: tuple[float, float]


def run_pipeline(params: SimulationParameters | None = None) -> BeamSteeringResult:
    """Run the full deterministic model pipeline."""
    p = params or SimulationParameters()
    energy = np.linspace(p.energy_min_ev, p.energy_max_ev, p.energy_points)
    gate = gate_grid(p.gate_min_v, p.gate_max_v, p.gate_points)
    linewidth = exciton_linewidth(gate)
    refl = reflection_map(energy, gate, linewidth, p.oscillator)
    reflectance = np.abs(refl) ** 2
    design_refl = complex_reflection(p.design_energy_ev, linewidth, p.oscillator)
    design_phase = unwrap_phase(design_refl)
    positions = metapixel_positions(p.metapixel_count, p.metapixel_spacing_m)
    target_angles = np.array(p.target_angles_deg, dtype=float)
    scan_angles = np.linspace(*p.scan_angles_deg)

    voltage_profiles: dict[float, np.ndarray] = {}
    phase_profiles: dict[float, np.ndarray] = {}
    far_field: dict[float, np.ndarray] = {}
    peaks: dict[float, float] = {}

    for target in target_angles:
        target_phase = phase_gradient_for_angle(positions, p.wavelength_m, float(target))
        voltages = inverse_gate_for_phase(gate, design_refl, target_phase)
        chosen_reflection = complex_reflection(p.design_energy_ev, exciton_linewidth(voltages), p.oscillator)
        chosen_phase = normalize_phase(phase(chosen_reflection))
        chosen_amp = amplitude(chosen_reflection)
        intensity = array_factor(positions, chosen_phase, p.wavelength_m, scan_angles, chosen_amp)
        voltage_profiles[float(target)] = voltages
        phase_profiles[float(target)] = chosen_phase
        far_field[float(target)] = intensity
        peaks[float(target)] = steering_peak_angle(scan_angles, intensity)

    return BeamSteeringResult(
        params=p,
        energy_ev=energy,
        gate_voltage_v=gate,
        linewidth_ev=linewidth,
        reflection=refl,
        reflectance=reflectance,
        design_reflection=design_refl,
        design_amplitude=amplitude(design_refl),
        design_phase_rad=design_phase,
        positions_m=positions,
        target_angles_deg=target_angles,
        voltage_profiles_v=voltage_profiles,
        phase_profiles_rad=phase_profiles,
        far_field_angles_deg=scan_angles,
        far_field_intensity=far_field,
        far_field_peak_deg=peaks,
        polariton_energies_ev=polariton_energies(p.oscillator),
    )
