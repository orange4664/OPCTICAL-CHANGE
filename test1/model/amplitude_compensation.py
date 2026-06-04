"""Amplitude-stability comparison for one-layer and two-layer TMD designs."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class AmplitudeCompensationResult:
    phase_rad: np.ndarray
    one_layer_amplitude: np.ndarray
    two_layer_amplitude: np.ndarray


def amplitude_compensation_curve(points: int = 361) -> AmplitudeCompensationResult:
    """Return deterministic amplitude curves over a 2*pi phase window."""
    phase_rad = np.linspace(-np.pi, np.pi, points)
    one_layer = 0.36 + 0.58 * (0.5 + 0.5 * np.cos(phase_rad - 0.15)) ** 1.4
    compensation = 0.18 * np.cos(phase_rad + 1.10) + 0.08 * np.cos(2.0 * phase_rad - 0.45)
    two_layer = np.clip(0.74 + compensation, 0.58, 0.95)
    return AmplitudeCompensationResult(phase_rad, one_layer, two_layer)


def amplitude_variation(values: np.ndarray) -> float:
    """Return peak-to-valley amplitude variation."""
    arr = np.asarray(values, dtype=float)
    return float(np.max(arr) - np.min(arr))
