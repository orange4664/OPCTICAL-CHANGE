"""Coupled-oscillator response for a hybrid-2D excitonic metasurface."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class CoupledOscillatorParameters:
    """Representative energy-domain parameters in eV."""

    cavity_energy_ev: float = 1.76
    exciton_energy_ev: float = 1.76
    coupling_ev: float = 0.080
    cavity_loss_ev: float = 0.004
    radiative_strength: float = 0.050
    background_amplitude: float = 1.00
    background_phase: float = 1.57


def polariton_energies(params: CoupledOscillatorParameters) -> tuple[float, float]:
    """Return approximate lower/upper polariton energies for zero detuning."""
    avg = 0.5 * (params.cavity_energy_ev + params.exciton_energy_ev)
    detuning = 0.5 * (params.cavity_energy_ev - params.exciton_energy_ev)
    split = np.sqrt(detuning**2 + params.coupling_ev**2)
    return float(avg - split), float(avg + split)


def complex_reflection(
    energy_ev: np.ndarray,
    exciton_linewidth_ev: np.ndarray,
    params: CoupledOscillatorParameters,
) -> np.ndarray:
    """Return complex reflection amplitude r(E,Vg)."""
    energy = np.asarray(energy_ev, dtype=float)
    linewidth = np.asarray(exciton_linewidth_ev, dtype=float)
    cavity = params.cavity_energy_ev - energy - 0.5j * params.cavity_loss_ev
    exciton = params.exciton_energy_ev - energy - 0.5j * linewidth
    denominator = cavity - params.coupling_ev**2 / exciton
    background = params.background_amplitude * np.exp(1j * params.background_phase)
    return background - params.radiative_strength / denominator


def reflection_map(
    energy_ev: np.ndarray,
    gate_voltage_v: np.ndarray,
    linewidth_ev: np.ndarray,
    params: CoupledOscillatorParameters,
) -> np.ndarray:
    """Return r(E,Vg) with shape (energy, gate)."""
    energy = np.asarray(energy_ev, dtype=float)[:, None]
    linewidth = np.asarray(linewidth_ev, dtype=float)[None, :]
    _ = np.asarray(gate_voltage_v, dtype=float)
    return complex_reflection(energy, linewidth, params)
