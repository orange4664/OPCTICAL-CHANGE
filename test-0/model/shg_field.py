"""Coherent bilayer SHG field model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class FieldParameters:
    """Coherent field-sum parameters."""

    stacking_phase: float = np.pi
    top_amplitude: float = 1.0
    bottom_amplitude: float = 1.0


def coherent_shg_field(
    chi_top: np.ndarray,
    chi_bottom: np.ndarray,
    params: FieldParameters | None = None,
) -> np.ndarray:
    """Compute scalar complex SHG field from two layer susceptibilities."""

    params = params or FieldParameters()
    phase = np.exp(1j * params.stacking_phase)
    return params.top_amplitude * chi_top + params.bottom_amplitude * phase * chi_bottom


def field_observables(field: np.ndarray) -> dict[str, np.ndarray]:
    """Return intensity, phase, real part, and imaginary part."""

    field = np.asarray(field)
    return {
        "intensity": np.abs(field) ** 2,
        "phase": np.angle(field),
        "real": np.real(field),
        "imag": np.imag(field),
    }


def normalize_intensity(intensity: np.ndarray) -> np.ndarray:
    """Normalize intensity by its finite maximum."""

    intensity = np.asarray(intensity, dtype=float)
    finite = np.isfinite(intensity)
    if not np.any(finite):
        return np.zeros_like(intensity)
    max_value = np.max(intensity[finite])
    if max_value <= 0:
        return np.zeros_like(intensity)
    return intensity / max_value

