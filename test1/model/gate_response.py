"""Gate-voltage control parameters for excitonic metapixels."""

from __future__ import annotations

import numpy as np


def gate_grid(v_min: float = -3.0, v_max: float = 3.0, points: int = 241) -> np.ndarray:
    """Return a deterministic gate-voltage grid in volts."""
    if points < 3:
        raise ValueError("points must be at least 3")
    return np.linspace(v_min, v_max, points)


def carrier_control(voltage: np.ndarray, scale: float = 1.25) -> np.ndarray:
    """Map gate voltage to a bounded carrier-control coordinate."""
    return 0.5 * (1.0 + np.tanh(np.asarray(voltage, dtype=float) / scale))


def exciton_linewidth(
    voltage: np.ndarray,
    base_mev: float = 8.0,
    gate_broadening_mev: float = 320.0,
    scale: float = 0.95,
) -> np.ndarray:
    """Gate-dependent exciton linewidth in eV."""
    control = carrier_control(voltage, scale=scale)
    linewidth_mev = base_mev + gate_broadening_mev * control
    return linewidth_mev / 1000.0
