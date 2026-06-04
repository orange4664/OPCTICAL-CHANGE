"""Zero finding and phase-winding diagnostics."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class FeasibilityBounds:
    """Lightweight experimental-feasibility filters in normalized units."""

    max_abs_gate: float = 4.0
    max_abs_displacement: float = 4.0
    min_relative_intensity: float = 1e-4


def nearest_zero_index(field: np.ndarray) -> tuple[int, int]:
    """Return index of the smallest absolute complex field."""

    flat = int(np.nanargmin(np.abs(field)))
    return np.unravel_index(flat, field.shape)


def phase_winding(field_values: np.ndarray) -> float:
    """Compute phase winding number around a closed complex-field path."""

    field_values = np.asarray(field_values)
    if field_values.ndim != 1:
        raise ValueError("field_values must be one-dimensional")
    if field_values.size < 4:
        raise ValueError("closed path needs at least four samples")
    phases = np.unwrap(np.angle(field_values))
    return float((phases[-1] - phases[0]) / (2.0 * np.pi))


def sample_loop(
    grid_x: np.ndarray,
    grid_y: np.ndarray,
    field: np.ndarray,
    center: tuple[float, float],
    radius: float,
    samples: int = 240,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Sample field values on an approximate circular loop using nearest grid cells."""

    theta = np.linspace(0.0, 2.0 * np.pi, samples, endpoint=True)
    x_path = center[0] + radius * np.cos(theta)
    y_path = center[1] + radius * np.sin(theta)
    x_axis = grid_x[0, :]
    y_axis = grid_y[:, 0]
    ix = np.searchsorted(x_axis, x_path)
    iy = np.searchsorted(y_axis, y_path)
    ix = np.clip(ix, 1, len(x_axis) - 1)
    iy = np.clip(iy, 1, len(y_axis) - 1)
    ix -= np.abs(x_path - x_axis[ix - 1]) < np.abs(x_path - x_axis[ix])
    iy -= np.abs(y_path - y_axis[iy - 1]) < np.abs(y_path - y_axis[iy])
    return x_path, y_path, field[iy, ix]


def feasibility_mask(
    top_voltage: np.ndarray,
    bottom_voltage: np.ndarray,
    displacement: np.ndarray,
    relative_intensity: np.ndarray,
    bounds: FeasibilityBounds | None = None,
) -> np.ndarray:
    """Return mask of points inside lightweight feasibility bounds."""

    bounds = bounds or FeasibilityBounds()
    gate_ok = (
        (np.abs(top_voltage) <= bounds.max_abs_gate)
        & (np.abs(bottom_voltage) <= bounds.max_abs_gate)
    )
    displacement_ok = np.abs(displacement) <= bounds.max_abs_displacement
    intensity_ok = relative_intensity >= bounds.min_relative_intensity
    return gate_ok & displacement_ok & intensity_ok

