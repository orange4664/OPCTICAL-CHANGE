"""Gate-voltage coordinate transforms for a dual-gated bilayer model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class GateParameters:
    """Minimal dual-gate calibration parameters.

    The capacitances are normalized model units. The model is intended for
    qualitative-to-semiquantitative scans, not extraction of device constants.
    """

    top_cap: float = 1.0
    bottom_cap: float = 1.0
    top_offset: float = 0.0
    bottom_offset: float = 0.0
    charge_unit: float = 1.0
    displacement_scale: float = 0.5


def gate_to_density_displacement(
    top_voltage: np.ndarray,
    bottom_voltage: np.ndarray,
    params: GateParameters | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Convert top/bottom gate voltage arrays to normalized carrier density and D.

    Returns:
        A tuple ``(density, displacement)`` in normalized model units.
    """

    params = params or GateParameters()
    vt = np.asarray(top_voltage, dtype=float) - params.top_offset
    vb = np.asarray(bottom_voltage, dtype=float) - params.bottom_offset
    density = (params.top_cap * vt + params.bottom_cap * vb) / params.charge_unit
    displacement = params.displacement_scale * (
        params.top_cap * vt - params.bottom_cap * vb
    )
    return density, displacement


def layer_density_split(
    density: np.ndarray,
    displacement: np.ndarray,
    polarization_scale: float = 1.5,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Split total density into top/bottom layer densities with smooth polarization.

    Positive displacement biases carriers toward the top layer. The returned
    layer densities are normalized, non-negative proxies used to tune oscillator
    strengths and resonance shifts.
    """

    density = np.asarray(density, dtype=float)
    displacement = np.asarray(displacement, dtype=float)
    carrier = np.maximum(density, 0.0)
    layer_polarization = np.tanh(displacement / polarization_scale)
    top = 0.5 * carrier * (1.0 + layer_polarization)
    bottom = 0.5 * carrier * (1.0 - layer_polarization)
    return top, bottom, layer_polarization


def gate_grid(
    vmin: float = -4.0,
    vmax: float = 4.0,
    points: int = 301,
) -> tuple[np.ndarray, np.ndarray]:
    """Return a square top/bottom gate mesh."""

    axis = np.linspace(vmin, vmax, points)
    return np.meshgrid(axis, axis, indexing="xy")

