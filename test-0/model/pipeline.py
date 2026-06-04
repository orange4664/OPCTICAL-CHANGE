"""End-to-end model assembly helpers."""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .gate_coordinates import (
    GateParameters,
    gate_grid,
    gate_to_density_displacement,
    layer_density_split,
)
from .shg_field import coherent_shg_field, field_observables, normalize_intensity
from .susceptibility import SusceptibilityParameters, layer_pair_susceptibility


@dataclass(frozen=True)
class ModelResult:
    top_voltage: np.ndarray
    bottom_voltage: np.ndarray
    density: np.ndarray
    displacement: np.ndarray
    top_density: np.ndarray
    bottom_density: np.ndarray
    chi_top: np.ndarray
    chi_bottom: np.ndarray
    field: np.ndarray
    intensity: np.ndarray
    relative_intensity: np.ndarray
    phase: np.ndarray
    real: np.ndarray
    imag: np.ndarray


def run_model(
    points: int = 301,
    gate_params: GateParameters | None = None,
    susceptibility_params: SusceptibilityParameters | None = None,
) -> ModelResult:
    """Run the full scalar complex-SHG model on a gate grid."""

    top_voltage, bottom_voltage = gate_grid(points=points)
    density, displacement = gate_to_density_displacement(
        top_voltage, bottom_voltage, gate_params
    )
    top_density, bottom_density, _ = layer_density_split(density, displacement)
    chi_top, chi_bottom = layer_pair_susceptibility(
        top_density, bottom_density, displacement, susceptibility_params
    )
    field = coherent_shg_field(chi_top, chi_bottom)
    observables = field_observables(field)
    relative_intensity = normalize_intensity(observables["intensity"])
    return ModelResult(
        top_voltage=top_voltage,
        bottom_voltage=bottom_voltage,
        density=density,
        displacement=displacement,
        top_density=top_density,
        bottom_density=bottom_density,
        chi_top=chi_top,
        chi_bottom=chi_bottom,
        field=field,
        intensity=observables["intensity"],
        relative_intensity=relative_intensity,
        phase=observables["phase"],
        real=observables["real"],
        imag=observables["imag"],
    )

