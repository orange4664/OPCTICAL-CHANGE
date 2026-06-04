"""Generate multi-panel figures for the complex-SHG proposal model."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from model.heterodyne import heterodyne_intensity, phase_shift_from_field
from model.pipeline import run_model
from model.shg_field import normalize_intensity
from model.susceptibility import SusceptibilityParameters
from model.topology import nearest_zero_index, phase_winding, sample_loop


def _save(fig: plt.Figure, output_dir: Path, name: str) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    fig.savefig(output_dir / f"{name}.png", dpi=220, bbox_inches="tight")
    fig.savefig(output_dir / f"{name}.pdf", bbox_inches="tight")
    plt.close(fig)


def _imshow(ax: plt.Axes, data: np.ndarray, title: str, cmap: str = "viridis") -> None:
    image = ax.imshow(
        data,
        origin="lower",
        extent=(-4, 4, -4, 4),
        cmap=cmap,
        aspect="equal",
    )
    ax.set_title(title)
    ax.set_xlabel("$V_t$ (norm.)")
    ax.set_ylabel("$V_b$ (norm.)")
    plt.colorbar(image, ax=ax, fraction=0.046, pad=0.04)


def figure_setup(result, output_dir: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(9.2, 7.4))
    ax = axes[0, 0]
    ax.plot([-4, 4], [4, -4], color="black", lw=1.8, label="constant n")
    ax.plot([-4, 4], [-4, 4], color="tab:red", lw=1.8, label="constant D")
    ax.set_title("Dual-gate coordinates")
    ax.set_xlabel("$V_t$")
    ax.set_ylabel("$V_b$")
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)
    ax.legend(frameon=False)

    ax = axes[0, 1]
    x = np.linspace(-3, 3, 300)
    top = 0.5 * (1 + np.tanh(x / 1.2))
    bottom = 1 - top
    ax.plot(x, top, label="top layer")
    ax.plot(x, bottom, label="bottom layer")
    ax.set_title("Layer-selective carrier proxy")
    ax.set_xlabel("displacement coordinate")
    ax.set_ylabel("relative carrier weight")
    ax.legend(frameon=False)

    ax = axes[1, 0]
    ax.text(0.5, 0.66, r"$E_{2\omega}=\chi_t^{(2)}- \chi_b^{(2)}$", ha="center", fontsize=18)
    ax.text(0.5, 0.42, "2H bilayer: opposite layer response", ha="center")
    ax.text(0.5, 0.25, "new observables: Re(E), Im(E), |E|^2, arg(E)", ha="center")
    ax.set_axis_off()
    ax.set_title("Scalar coherent SHG sum")

    ax = axes[1, 1]
    idx = nearest_zero_index(result.field)
    ax.imshow(result.relative_intensity, origin="lower", extent=(-4, 4, -4, 4), cmap="magma")
    ax.scatter(result.top_voltage[idx], result.bottom_voltage[idx], s=90, facecolors="none", edgecolors="cyan", lw=2)
    ax.set_title("Model-predicted near-zero")
    ax.set_xlabel("$V_t$")
    ax.set_ylabel("$V_b$")

    fig.suptitle("Figure 1. Innovation setup and model coordinates")
    fig.tight_layout()
    _save(fig, output_dir, "figure_1_setup_coordinates")


def figure_complex_maps(result, output_dir: Path) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(9.4, 7.8))
    _imshow(axes[0, 0], np.log10(result.relative_intensity + 1e-7), r"$\log_{10}(|E|^2)$", "magma")
    _imshow(axes[0, 1], result.phase, r"$\arg(E)$", "twilight")
    _imshow(axes[1, 0], result.real, r"$\mathrm{Re}(E)$", "coolwarm")
    _imshow(axes[1, 1], result.imag, r"$\mathrm{Im}(E)$", "coolwarm")
    idx = nearest_zero_index(result.field)
    for ax in axes.flat:
        ax.scatter(result.top_voltage[idx], result.bottom_voltage[idx], s=70, facecolors="none", edgecolors="cyan", lw=1.8)
    fig.suptitle("Figure 2. Scalar complex SHG field maps")
    fig.tight_layout()
    _save(fig, output_dir, "figure_2_complex_field_maps")


def figure_path(result, output_dir: Path) -> None:
    idx = nearest_zero_index(result.field)
    center = (float(result.top_voltage[idx]), float(result.bottom_voltage[idx]))
    x_path, y_path, values = sample_loop(
        result.top_voltage, result.bottom_voltage, result.field, center, radius=0.75
    )
    winding = phase_winding(values)
    rel = normalize_intensity(np.abs(values) ** 2)
    phase = phase_shift_from_field(values)

    fig, axes = plt.subplots(2, 2, figsize=(9.4, 7.7))
    axes[0, 0].imshow(result.relative_intensity, origin="lower", extent=(-4, 4, -4, 4), cmap="magma")
    axes[0, 0].plot(x_path, y_path, color="cyan", lw=2)
    axes[0, 0].set_title("Gate loop around zero")
    axes[0, 0].set_xlabel("$V_t$")
    axes[0, 0].set_ylabel("$V_b$")

    axes[0, 1].plot(np.real(values), np.imag(values), color="tab:blue", lw=2)
    axes[0, 1].scatter([0], [0], color="black", s=30)
    axes[0, 1].set_aspect("equal", adjustable="box")
    axes[0, 1].set_title(f"Complex-plane trajectory, W={winding:.2f}")
    axes[0, 1].set_xlabel("Re(E)")
    axes[0, 1].set_ylabel("Im(E)")

    t = np.linspace(0, 1, len(values))
    axes[1, 0].plot(t, rel, color="tab:orange")
    axes[1, 0].set_title("Relative intensity along loop")
    axes[1, 0].set_xlabel("loop coordinate")
    axes[1, 0].set_ylabel("normalized |E|^2")

    axes[1, 1].plot(t, phase / np.pi, color="tab:green")
    axes[1, 1].set_title("Unwrapped phase")
    axes[1, 1].set_xlabel("loop coordinate")
    axes[1, 1].set_ylabel(r"phase / $\pi$")
    fig.suptitle("Figure 3. Gate loop and phase winding")
    fig.tight_layout()
    _save(fig, output_dir, "figure_3_gate_loop_winding")


def figure_robustness(result, output_dir: Path) -> None:
    widths = np.linspace(0.035, 0.085, 9)
    strengths = np.linspace(0.8, 1.6, 9)
    min_intensity = np.zeros((len(widths), len(strengths)))
    winding_map = np.zeros_like(min_intensity)
    idx0 = nearest_zero_index(result.field)
    center = (float(result.top_voltage[idx0]), float(result.bottom_voltage[idx0]))
    for i, width in enumerate(widths):
        for j, strength in enumerate(strengths):
            params = SusceptibilityParameters(
                polaron_width=float(width), polaron_strength=float(strength)
            )
            sweep = run_model(points=201, susceptibility_params=params)
            min_intensity[i, j] = np.min(sweep.relative_intensity)
            _, _, values = sample_loop(
                sweep.top_voltage, sweep.bottom_voltage, sweep.field, center, radius=0.75
            )
            winding_map[i, j] = phase_winding(values)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2))
    im0 = axes[0].imshow(
        np.log10(min_intensity + 1e-8),
        origin="lower",
        extent=(strengths[0], strengths[-1], widths[0], widths[-1]),
        aspect="auto",
        cmap="magma",
    )
    axes[0].set_title("Near-zero depth under parameter sweep")
    axes[0].set_xlabel("polaron oscillator strength")
    axes[0].set_ylabel("polaron linewidth")
    plt.colorbar(im0, ax=axes[0], label=r"$\log_{10}\min |E|^2$")

    im1 = axes[1].imshow(
        winding_map,
        origin="lower",
        extent=(strengths[0], strengths[-1], widths[0], widths[-1]),
        aspect="auto",
        cmap="coolwarm",
        vmin=-1.2,
        vmax=1.2,
    )
    axes[1].set_title("Loop winding diagnostic")
    axes[1].set_xlabel("polaron oscillator strength")
    axes[1].set_ylabel("polaron linewidth")
    plt.colorbar(im1, ax=axes[1], label="winding")
    fig.suptitle("Figure 4. Lightweight robustness and feasibility diagnostic")
    fig.tight_layout()
    _save(fig, output_dir, "figure_4_robustness")


def figure_heterodyne(result, output_dir: Path) -> None:
    idx = nearest_zero_index(result.field)
    center = (float(result.top_voltage[idx]), float(result.bottom_voltage[idx]))
    _, _, values = sample_loop(
        result.top_voltage, result.bottom_voltage, result.field, center, radius=0.75
    )
    path_idx = np.linspace(0, len(values) - 1, 80).astype(int)
    sampled = values[path_idx]
    reference_phase = np.linspace(0, 2 * np.pi, 140)
    fringes = heterodyne_intensity(sampled, reference_phase, reference_amplitude=3.0)
    fringe_phase = phase_shift_from_field(sampled)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4.4))
    im = axes[0].imshow(
        fringes,
        origin="lower",
        aspect="auto",
        extent=(0, 2, 0, 1),
        cmap="viridis",
    )
    axes[0].set_title("Simulated heterodyne fringes")
    axes[0].set_xlabel(r"reference phase / $\pi$")
    axes[0].set_ylabel("gate-loop coordinate")
    plt.colorbar(im, ax=axes[0], label="interference intensity")

    axes[1].plot(np.linspace(0, 1, len(fringe_phase)), fringe_phase / np.pi, color="tab:purple")
    axes[1].set_title("Retrieved sample phase shift")
    axes[1].set_xlabel("gate-loop coordinate")
    axes[1].set_ylabel(r"phase / $\pi$")
    fig.suptitle("Figure 5. Heterodyne SHG observable")
    fig.tight_layout()
    _save(fig, output_dir, "figure_5_heterodyne")


def generate_all(output_dir: Path, points: int = 301) -> None:
    result = run_model(points=points)
    figure_setup(result, output_dir)
    figure_complex_maps(result, output_dir)
    figure_path(result, output_dir)
    figure_robustness(result, output_dir)
    figure_heterodyne(result, output_dir)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", default="output/figures", type=Path)
    parser.add_argument("--points", default=301, type=int)
    args = parser.parse_args()
    generate_all(args.output_dir, points=args.points)


if __name__ == "__main__":
    main()
