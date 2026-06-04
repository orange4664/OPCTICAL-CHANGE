"""Layer-resolved complex susceptibility model."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class SusceptibilityParameters:
    """Phenomenological Lorentz-oscillator parameters in eV-like units."""

    photon_energy: float = 1.72
    neutral_energy: float = 1.72
    polaron_energy: float = 1.665
    neutral_width: float = 0.035
    polaron_width: float = 0.055
    neutral_strength: float = 1.0
    polaron_strength: float = 1.25
    density_scale: float = 2.0
    displacement_shift: float = 0.012
    background: complex = 0.05 + 0.02j


def lorentz_response(
    energy: np.ndarray | float,
    resonance: np.ndarray | float,
    width: np.ndarray | float,
    strength: np.ndarray | float,
) -> np.ndarray:
    """Return a complex Lorentz response with resonant phase rotation."""

    return np.asarray(strength) / (
        np.asarray(resonance) - np.asarray(energy) - 1j * np.asarray(width)
    )


def layer_susceptibility(
    layer_density: np.ndarray,
    displacement: np.ndarray,
    layer_sign: float,
    params: SusceptibilityParameters | None = None,
) -> np.ndarray:
    """Compute one layer's complex chi2 proxy.

    ``layer_sign`` is +1 for top and -1 for bottom, shifting the resonance in
    opposite directions under displacement.
    """

    params = params or SusceptibilityParameters()
    layer_density = np.asarray(layer_density, dtype=float)
    displacement = np.asarray(displacement, dtype=float)
    occupancy = layer_density / (layer_density + params.density_scale)
    neutral_weight = params.neutral_strength * (1.0 - occupancy)
    polaron_weight = params.polaron_strength * occupancy
    shift = layer_sign * params.displacement_shift * np.tanh(displacement / 2.0)
    neutral = lorentz_response(
        params.photon_energy,
        params.neutral_energy + shift,
        params.neutral_width,
        neutral_weight,
    )
    polaron = lorentz_response(
        params.photon_energy,
        params.polaron_energy + 0.5 * shift,
        params.polaron_width,
        polaron_weight,
    )
    return params.background + neutral + polaron


def layer_pair_susceptibility(
    top_density: np.ndarray,
    bottom_density: np.ndarray,
    displacement: np.ndarray,
    params: SusceptibilityParameters | None = None,
) -> tuple[np.ndarray, np.ndarray]:
    """Return top and bottom layer susceptibilities."""

    params = params or SusceptibilityParameters()
    chi_top = layer_susceptibility(top_density, displacement, +1.0, params)
    chi_bottom = layer_susceptibility(bottom_density, displacement, -1.0, params)
    return chi_top, chi_bottom

