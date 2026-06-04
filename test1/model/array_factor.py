"""One-dimensional phased-array far-field model."""

from __future__ import annotations

import numpy as np


def metapixel_positions(count: int = 96, spacing_m: float = 0.32e-6) -> np.ndarray:
    """Return centered metapixel positions in meters."""
    if count < 2:
        raise ValueError("count must be at least 2")
    idx = np.arange(count, dtype=float) - 0.5 * (count - 1)
    return idx * spacing_m


def array_factor(
    positions_m: np.ndarray,
    phases_rad: np.ndarray,
    wavelength_m: float,
    angles_deg: np.ndarray,
    amplitudes: np.ndarray | None = None,
) -> np.ndarray:
    """Return normalized far-field intensity versus angle."""
    positions = np.asarray(positions_m, dtype=float)
    phases = np.asarray(phases_rad, dtype=float)
    angles = np.asarray(angles_deg, dtype=float)
    if amplitudes is None:
        weights = np.ones_like(phases)
    else:
        weights = np.asarray(amplitudes, dtype=float)
    if positions.shape != phases.shape or positions.shape != weights.shape:
        raise ValueError("positions, phases, and amplitudes must have matching shapes")
    k0 = 2.0 * np.pi / wavelength_m
    scan_phase = k0 * np.sin(np.deg2rad(angles))[:, None] * positions[None, :]
    field = np.sum(weights[None, :] * np.exp(1j * (phases[None, :] - scan_phase)), axis=1)
    intensity = np.abs(field) ** 2
    peak = np.max(intensity)
    return intensity / peak if peak > 0 else intensity


def steering_peak_angle(angles_deg: np.ndarray, intensity: np.ndarray) -> float:
    """Return the angle of the strongest lobe."""
    angles = np.asarray(angles_deg, dtype=float)
    return float(angles[int(np.argmax(intensity))])
