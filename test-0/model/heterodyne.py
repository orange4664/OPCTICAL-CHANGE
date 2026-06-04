"""Heterodyne SHG observable simulation."""

from __future__ import annotations

import numpy as np


def heterodyne_intensity(
    sample_field: np.ndarray,
    reference_phase: np.ndarray,
    reference_amplitude: float = 1.0,
) -> np.ndarray:
    """Return interference intensity against a reference SHG field."""

    sample_field = np.asarray(sample_field)
    reference_phase = np.asarray(reference_phase)
    reference = reference_amplitude * np.exp(1j * reference_phase)
    return np.abs(sample_field[..., None] + reference) ** 2


def phase_shift_from_field(sample_field: np.ndarray) -> np.ndarray:
    """Return the expected fringe phase shift from a complex field."""

    return np.unwrap(np.angle(sample_field))

