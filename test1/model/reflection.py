"""Complex-reflection helpers and inverse gate lookup."""

from __future__ import annotations

import numpy as np


def amplitude(values: np.ndarray) -> np.ndarray:
    return np.abs(values)


def phase(values: np.ndarray) -> np.ndarray:
    return np.angle(values)


def unwrap_phase(values: np.ndarray) -> np.ndarray:
    return np.unwrap(np.angle(values))


def normalize_phase(values: np.ndarray) -> np.ndarray:
    """Normalize phase to [0, 2*pi)."""
    return np.mod(values, 2 * np.pi)


def inverse_gate_for_phase(
    gate_voltage_v: np.ndarray,
    reflection_values: np.ndarray,
    target_phase_rad: np.ndarray,
) -> np.ndarray:
    """Pick the gate voltage whose reflection phase best matches each target."""
    gate = np.asarray(gate_voltage_v, dtype=float)
    phases = normalize_phase(unwrap_phase(reflection_values))
    targets = normalize_phase(np.asarray(target_phase_rad, dtype=float))
    diff = np.angle(np.exp(1j * (targets[..., None] - phases[None, ...])))
    indices = np.argmin(np.abs(diff), axis=-1)
    return gate[indices]


def phase_gradient_for_angle(
    positions_m: np.ndarray,
    wavelength_m: float,
    angle_deg: float,
) -> np.ndarray:
    """Return target phase profile for a reflected steering angle."""
    k0 = 2.0 * np.pi / wavelength_m
    angle_rad = np.deg2rad(angle_deg)
    return normalize_phase(k0 * np.asarray(positions_m, dtype=float) * np.sin(angle_rad))
