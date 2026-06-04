"""Generate deterministic simulation figures for the test1 proposal."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

from model.amplitude_compensation import amplitude_variation
from model.pipeline import BeamSteeringResult, run_pipeline
from model.reflection import phase_gradient_for_angle


FIGURE_BASENAMES = (
    "figure_1_strong_coupling_gate_tuning",
    "figure_2_complex_reflection_coefficient",
    "figure_3_inverse_gate_profile",
    "figure_4_programmable_beam_steering",
    "figure_5_amplitude_compensation",
)

COLORS = {
    "neutral": "#25313d",
    "muted": "#6b7280",
    "blue": "#2563eb",
    "teal": "#0f766e",
    "orange": "#d97706",
    "red": "#dc2626",
    "purple": "#7c3aed",
}


def _configure_style() -> None:
    mpl.rcParams.update(
        {
            "font.family": "sans-serif",
            "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans", "sans-serif"],
            "pdf.fonttype": 42,
            "svg.fonttype": "none",
            "font.size": 10,
            "axes.titlesize": 12,
            "axes.labelsize": 10,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9,
            "legend.fontsize": 9,
            "axes.spines.right": False,
            "axes.spines.top": False,
            "axes.linewidth": 0.9,
            "lines.linewidth": 2.0,
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )


def _save(fig: mpl.figure.Figure, output_dir: Path, basename: str) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    paths = [output_dir / f"{basename}.png", output_dir / f"{basename}.pdf"]
    for path in paths:
        if path.suffix == ".png":
            fig.savefig(path, dpi=320, bbox_inches="tight")
        else:
            fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return paths


def _panel_label(ax: mpl.axes.Axes, label: str) -> None:
    ax.text(
        -0.12,
        1.06,
        label,
        transform=ax.transAxes,
        fontsize=12,
        fontweight="bold",
        va="bottom",
        ha="left",
    )


def _plot_figure_1(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    fig, (ax_map, ax_line) = plt.subplots(
        1,
        2,
        figsize=(10.2, 4.1),
        gridspec_kw={"width_ratios": [1.7, 1.0]},
        constrained_layout=True,
    )

    normalized = result.reflectance / np.nanmax(result.reflectance)
    mesh = ax_map.pcolormesh(
        result.gate_voltage_v,
        result.energy_ev,
        normalized,
        shading="auto",
        cmap="magma",
        rasterized=True,
    )
    lower, upper = result.polariton_energies_ev
    ax_map.axhline(lower, color="white", linestyle="--", linewidth=1.2, label="LP / UP")
    ax_map.axhline(upper, color="white", linestyle="--", linewidth=1.2)
    ax_map.axhline(
        result.params.design_energy_ev,
        color="#7dd3fc",
        linestyle="-",
        linewidth=1.4,
        label="design energy",
    )
    ax_map.set_title("Gate-tuned coupled-oscillator map")
    ax_map.set_xlabel("Gate voltage (V)")
    ax_map.set_ylabel("Photon energy (eV)")
    ax_map.legend(loc="lower left")
    colorbar = fig.colorbar(mesh, ax=ax_map, pad=0.02)
    colorbar.set_label("Normalized reflectance")
    _panel_label(ax_map, "a")

    ax_line.plot(
        result.gate_voltage_v,
        result.linewidth_ev * 1000.0,
        color=COLORS["red"],
    )
    ax_line.fill_between(
        result.gate_voltage_v,
        0,
        result.linewidth_ev * 1000.0,
        color=COLORS["red"],
        alpha=0.12,
        linewidth=0,
    )
    ax_line.set_title("Electrical broadening")
    ax_line.set_xlabel("Gate voltage (V)")
    ax_line.set_ylabel("Exciton linewidth (meV)")
    ax_line.text(
        0.04,
        0.92,
        "strong-coupling window narrows\nas non-radiative loss rises",
        transform=ax_line.transAxes,
        ha="left",
        va="top",
        color=COLORS["neutral"],
    )
    ax_line.grid(alpha=0.22)
    _panel_label(ax_line, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[0])


def _plot_figure_2(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    fig, (ax_complex, ax_gate) = plt.subplots(
        1,
        2,
        figsize=(10.0, 4.0),
        gridspec_kw={"width_ratios": [1.0, 1.25]},
        constrained_layout=True,
    )

    sc = ax_complex.scatter(
        result.design_reflection.real,
        result.design_reflection.imag,
        c=result.gate_voltage_v,
        cmap="viridis",
        s=20,
        linewidth=0,
    )
    ax_complex.plot(
        result.design_reflection.real,
        result.design_reflection.imag,
        color=COLORS["muted"],
        alpha=0.45,
        linewidth=1.2,
    )
    ax_complex.axhline(0, color="#d1d5db", linewidth=0.8)
    ax_complex.axvline(0, color="#d1d5db", linewidth=0.8)
    ax_complex.set_aspect("equal", adjustable="box")
    ax_complex.set_title("Complex reflection path")
    ax_complex.set_xlabel("Re(r)")
    ax_complex.set_ylabel("Im(r)")
    cbar = fig.colorbar(sc, ax=ax_complex, pad=0.02)
    cbar.set_label("Gate voltage (V)")
    _panel_label(ax_complex, "a")

    phase_pi = np.unwrap(np.angle(result.design_reflection)) / np.pi
    ax_gate.plot(
        result.gate_voltage_v,
        result.design_amplitude,
        color=COLORS["blue"],
        label="Amplitude |r|",
    )
    ax_gate.set_xlabel("Gate voltage (V)")
    ax_gate.set_ylabel("Amplitude |r|", color=COLORS["blue"])
    ax_gate.tick_params(axis="y", labelcolor=COLORS["blue"])
    ax_phase = ax_gate.twinx()
    ax_phase.plot(
        result.gate_voltage_v,
        phase_pi,
        color=COLORS["orange"],
        label="Phase",
    )
    ax_phase.set_ylabel("Unwrapped phase / pi", color=COLORS["orange"])
    ax_phase.tick_params(axis="y", labelcolor=COLORS["orange"])
    ax_gate.set_title(f"Response at {result.params.design_energy_ev:.3f} eV")
    ax_gate.grid(alpha=0.22)
    lines = ax_gate.get_lines() + ax_phase.get_lines()
    labels = [line.get_label() for line in lines]
    ax_gate.legend(lines, labels, loc="best")
    _panel_label(ax_gate, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[1])


def _plot_figure_3(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    fig, (ax_voltage, ax_phase) = plt.subplots(
        1,
        2,
        figsize=(10.2, 4.0),
        constrained_layout=True,
    )
    pixel = np.arange(result.params.metapixel_count)
    line_colors = [COLORS["neutral"], COLORS["teal"], COLORS["orange"]]

    for color, target in zip(line_colors, result.target_angles_deg, strict=True):
        profile = result.voltage_profiles_v[float(target)]
        ax_voltage.plot(pixel, profile, color=color, label=f"{target:.0f} deg")
    ax_voltage.set_title("Inverse-designed gate profile")
    ax_voltage.set_xlabel("Metapixel index")
    ax_voltage.set_ylabel("Gate voltage (V)")
    ax_voltage.legend(title="Target angle")
    ax_voltage.grid(alpha=0.22)
    _panel_label(ax_voltage, "a")

    target = float(result.target_angles_deg[-1])
    desired = phase_gradient_for_angle(
        result.positions_m,
        result.params.wavelength_m,
        target,
    )
    achieved = result.phase_profiles_rad[target]
    ax_phase.plot(pixel, desired / np.pi, color=COLORS["muted"], label="target phase")
    ax_phase.scatter(
        pixel,
        achieved / np.pi,
        s=16,
        color=COLORS["purple"],
        alpha=0.85,
        label="gate-selected phase",
    )
    ax_phase.set_title(f"Phase matching for {target:.0f} deg steering")
    ax_phase.set_xlabel("Metapixel index")
    ax_phase.set_ylabel("Phase / pi")
    ax_phase.legend(loc="best")
    ax_phase.grid(alpha=0.22)
    _panel_label(ax_phase, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[2])


def _plot_figure_4(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    fig, (ax_far, ax_peak) = plt.subplots(
        1,
        2,
        figsize=(10.2, 4.0),
        gridspec_kw={"width_ratios": [1.55, 1.0]},
        constrained_layout=True,
    )
    line_colors = [COLORS["neutral"], COLORS["teal"], COLORS["orange"]]

    for color, target in zip(line_colors, result.target_angles_deg, strict=True):
        target_key = float(target)
        peak = result.far_field_peak_deg[target_key]
        ax_far.plot(
            result.far_field_angles_deg,
            result.far_field_intensity[target_key],
            color=color,
            label=f"target {target:.0f} deg, peak {peak:.1f} deg",
        )
        ax_far.axvline(peak, color=color, linestyle=":", linewidth=1.0, alpha=0.7)
    ax_far.set_title("Programmable far-field steering")
    ax_far.set_xlabel("Observation angle (deg)")
    ax_far.set_ylabel("Normalized intensity")
    ax_far.set_xlim(-5, 30)
    ax_far.legend(loc="upper right")
    ax_far.grid(alpha=0.22)
    _panel_label(ax_far, "a")

    targets = result.target_angles_deg
    peaks = np.array([result.far_field_peak_deg[float(t)] for t in targets])
    width = 0.36
    x = np.arange(len(targets))
    ax_peak.bar(x - width / 2, targets, width, color="#9ca3af", label="target")
    ax_peak.bar(x + width / 2, peaks, width, color=COLORS["teal"], label="simulated peak")
    ax_peak.plot(x, targets, color=COLORS["muted"], linewidth=1.0, alpha=0.45)
    ax_peak.set_xticks(x)
    ax_peak.set_xticklabels([f"{t:.0f}" for t in targets])
    ax_peak.set_title("Target-to-peak agreement")
    ax_peak.set_xlabel("Programmed angle (deg)")
    ax_peak.set_ylabel("Angle (deg)")
    ax_peak.legend(loc="upper left")
    ax_peak.grid(axis="y", alpha=0.22)
    _panel_label(ax_peak, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[3])


def _plot_figure_5(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    comp = result.amplitude_compensation
    one_span = amplitude_variation(comp.one_layer_amplitude)
    two_span = amplitude_variation(comp.two_layer_amplitude)

    fig, (ax_curve, ax_span) = plt.subplots(
        1,
        2,
        figsize=(10.0, 4.0),
        gridspec_kw={"width_ratios": [1.45, 0.9]},
        constrained_layout=True,
    )
    phase_pi = comp.phase_rad / np.pi

    ax_curve.plot(
        phase_pi,
        comp.one_layer_amplitude,
        color=COLORS["orange"],
        label="one-layer TMD",
    )
    ax_curve.plot(
        phase_pi,
        comp.two_layer_amplitude,
        color=COLORS["blue"],
        label="two-layer compensated",
    )
    ax_curve.set_title("Amplitude stability over phase control")
    ax_curve.set_xlabel("Phase / pi")
    ax_curve.set_ylabel("Reflection amplitude")
    ax_curve.set_xlim(-1, 1)
    ax_curve.set_ylim(0.2, 1.02)
    ax_curve.legend(loc="lower left")
    ax_curve.grid(alpha=0.22)
    _panel_label(ax_curve, "a")

    bars = ax_span.bar(
        [0, 1],
        [one_span, two_span],
        color=[COLORS["orange"], COLORS["blue"]],
        width=0.58,
    )
    ax_span.set_xticks([0, 1])
    ax_span.set_xticklabels(["one-layer", "two-layer"])
    ax_span.set_ylabel("Peak-to-valley amplitude span")
    ax_span.set_title("Compact support panel")
    ax_span.grid(axis="y", alpha=0.22)
    for bar, value in zip(bars, [one_span, two_span], strict=True):
        ax_span.text(
            bar.get_x() + bar.get_width() / 2,
            value + 0.02,
            f"{value:.2f}",
            ha="center",
            va="bottom",
            color=COLORS["neutral"],
        )
    ax_span.text(
        0.5,
        0.92,
        f"{100.0 * (1.0 - two_span / one_span):.0f}% lower span",
        transform=ax_span.transAxes,
        ha="center",
        va="top",
        color=COLORS["neutral"],
        fontweight="bold",
    )
    _panel_label(ax_span, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[4])


def generate_figures(output_dir: str | Path) -> list[Path]:
    """Run the simulation pipeline once and export all required figures."""
    _configure_style()
    out = Path(output_dir)
    result = run_pipeline()
    paths: list[Path] = []
    paths.extend(_plot_figure_1(result, out))
    paths.extend(_plot_figure_2(result, out))
    paths.extend(_plot_figure_3(result, out))
    paths.extend(_plot_figure_4(result, out))
    paths.extend(_plot_figure_5(result, out))
    return paths


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default=ROOT / "output" / "figures",
        type=Path,
        help="Directory for generated PNG/PDF figures.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = generate_figures(args.output_dir)
    print(f"Generated {len(paths)} files in {Path(args.output_dir).resolve()}")
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
