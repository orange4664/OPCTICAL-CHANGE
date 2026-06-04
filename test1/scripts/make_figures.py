"""Generate deterministic simulation figures for the test1 proposal."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib as mpl

mpl.use("Agg")

import matplotlib.pyplot as plt
import matplotlib.patheffects as pe
import numpy as np

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
    "ink": "#1f2933",
    "muted": "#667085",
    "grid": "#d0d5dd",
    "blue": "#3b6fb6",
    "cyan": "#2a9bb5",
    "teal": "#2f8f83",
    "orange": "#c47a2c",
    "red": "#c94c4c",
    "purple": "#7b61b7",
    "gold": "#b68b2c",
}

PDF_METADATA = {
    "CreationDate": datetime(2026, 6, 4, tzinfo=timezone.utc),
    "ModDate": datetime(2026, 6, 4, tzinfo=timezone.utc),
    "Creator": "test1/scripts/make_figures.py",
    "Producer": "Matplotlib",
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
            "legend.frameon": False,
            "xtick.major.size": 4,
            "ytick.major.size": 4,
            "xtick.direction": "out",
            "ytick.direction": "out",
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
            fig.savefig(path, bbox_inches="tight", metadata=PDF_METADATA)
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
        color=COLORS["ink"],
    )


def _format_axis(ax: mpl.axes.Axes, *, grid: bool = True) -> None:
    ax.tick_params(colors=COLORS["ink"], labelcolor=COLORS["ink"])
    ax.xaxis.label.set_color(COLORS["ink"])
    ax.yaxis.label.set_color(COLORS["ink"])
    ax.title.set_color(COLORS["ink"])
    if grid:
        ax.grid(color=COLORS["grid"], alpha=0.42, linewidth=0.8)


def _dark_plate_label(
    ax: mpl.axes.Axes,
    x: float,
    y: float,
    text: str,
    *,
    color: str = "white",
    ha: str = "left",
) -> None:
    ax.text(
        x,
        y,
        text,
        color=color,
        fontsize=8.5,
        ha=ha,
        va="center",
        bbox={
            "boxstyle": "round,pad=0.16",
            "facecolor": "#05070d",
            "edgecolor": "none",
            "alpha": 0.62,
        },
        path_effects=[pe.Stroke(linewidth=2.2, foreground="#05070d"), pe.Normal()],
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
    ax_map.axhline(lower, color="white", linestyle="--", linewidth=1.2)
    ax_map.axhline(upper, color="white", linestyle="--", linewidth=1.2)
    ax_map.axhline(
        result.params.design_energy_ev,
        color="#7dd3fc",
        linestyle="-",
        linewidth=1.4,
    )
    _dark_plate_label(ax_map, 2.88, upper + 0.014, "upper polariton", ha="right")
    _dark_plate_label(ax_map, 2.88, lower - 0.014, "lower polariton", ha="right")
    _dark_plate_label(
        ax_map,
        -2.85,
        result.params.design_energy_ev + 0.010,
        "design energy",
        color="#7dd3fc",
    )
    ax_map.set_title("Gate-tuned strong-coupling response")
    ax_map.set_xlabel("Gate voltage (V)")
    ax_map.set_ylabel("Photon energy (eV)")
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
    ax_line.set_title("Gate-induced exciton loss")
    ax_line.set_xlabel("Gate voltage (V)")
    ax_line.set_ylabel("Exciton linewidth (meV)")
    ax_line.text(
        0.04,
        0.92,
        "strong-coupling window narrows\nas non-radiative loss rises",
        transform=ax_line.transAxes,
        ha="left",
        va="top",
        color=COLORS["ink"],
    )
    _format_axis(ax_line)
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
    ax_complex.axhline(0, color=COLORS["grid"], linewidth=0.8)
    ax_complex.axvline(0, color=COLORS["grid"], linewidth=0.8)
    ax_complex.set_aspect("equal", adjustable="box")
    ax_complex.set_title("Complex reflection trajectory")
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
    ax_gate.set_title(f"Design-energy response ({result.params.design_energy_ev:.3f} eV)")
    _format_axis(ax_gate)
    ax_phase.spines["top"].set_visible(False)
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
    line_colors = [COLORS["ink"], COLORS["teal"], COLORS["orange"]]

    for color, target in zip(line_colors, result.target_angles_deg, strict=True):
        profile = result.voltage_profiles_v[float(target)]
        ax_voltage.plot(pixel, profile, color=color, label=f"{target:.0f} deg")
        label_y = float(profile[-1])
        if target == 20.0:
            label_y = 2.82
        ax_voltage.text(
            pixel[-1] + 2.0,
            label_y,
            f"{target:.0f} deg",
            color=color,
            fontsize=9,
            va="center",
            ha="left",
            clip_on=False,
        )
    ax_voltage.set_title("Inverse-designed voltage maps")
    ax_voltage.set_xlabel("Metapixel index")
    ax_voltage.set_ylabel("Gate voltage (V)")
    ax_voltage.set_xlim(-2, result.params.metapixel_count + 10)
    _format_axis(ax_voltage)
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
    ax_phase.set_title(f"Phase quantization for {target:.0f} deg steering")
    ax_phase.set_xlabel("Metapixel index")
    ax_phase.set_ylabel("Phase / pi")
    ax_phase.legend(loc="best")
    _format_axis(ax_phase)
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
    line_colors = [COLORS["ink"], COLORS["teal"], COLORS["orange"]]

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
    ax_far.set_title("Electrically programmed far field")
    ax_far.set_xlabel("Observation angle (deg)")
    ax_far.set_ylabel("Normalized intensity")
    ax_far.set_xlim(-5, 30)
    ax_far.legend(loc="upper right")
    _format_axis(ax_far)
    _panel_label(ax_far, "a")

    targets = result.target_angles_deg
    peaks = np.array([result.far_field_peak_deg[float(t)] for t in targets])
    width = 0.36
    x = np.arange(len(targets))
    ax_peak.bar(x - width / 2, targets, width, color="#a8b0bb", label="target")
    ax_peak.bar(x + width / 2, peaks, width, color=COLORS["teal"], label="simulated peak")
    ax_peak.plot(x, targets, color=COLORS["muted"], linewidth=1.0, alpha=0.45)
    ax_peak.set_xticks(x)
    ax_peak.set_xticklabels([f"{t:.0f}" for t in targets])
    ax_peak.set_title("Target-to-peak transfer")
    ax_peak.set_xlabel("Programmed angle (deg)")
    ax_peak.set_ylabel("Angle (deg)")
    ax_peak.legend(loc="upper left")
    _format_axis(ax_peak)
    _panel_label(ax_peak, "b")

    return _save(fig, output_dir, FIGURE_BASENAMES[3])


def _plot_figure_5(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    fig, (ax_curve, ax_span) = plt.subplots(
        1,
        2,
        figsize=(10.0, 4.0),
        gridspec_kw={"width_ratios": [1.35, 1.0]},
        constrained_layout=True,
    )

    energies = np.array([1.665, 1.680, result.params.design_energy_ev, 1.710, 1.725])
    phase_spans: list[float] = []
    amplitude_cv: list[float] = []
    line_colors = [COLORS["muted"], COLORS["cyan"], COLORS["blue"], COLORS["orange"], COLORS["red"]]

    for energy, color in zip(energies, line_colors, strict=True):
        idx = int(np.argmin(np.abs(result.energy_ev - energy)))
        response = result.reflection[idx, :]
        amp = np.abs(response)
        amp_norm = amp / np.mean(amp)
        phase_pi = np.unwrap(np.angle(response)) / np.pi
        phase_span = float(np.max(phase_pi) - np.min(phase_pi))
        phase_spans.append(phase_span)
        amplitude_cv.append(float(np.std(amp) / np.mean(amp)))
        label = f"{result.energy_ev[idx]:.3f} eV"
        alpha = 0.95 if abs(result.energy_ev[idx] - result.params.design_energy_ev) < 0.003 else 0.72
        linewidth = 2.6 if abs(result.energy_ev[idx] - result.params.design_energy_ev) < 0.003 else 1.8
        ax_curve.plot(phase_pi, amp_norm, color=color, alpha=alpha, linewidth=linewidth, label=label)

    ax_curve.set_title("Phase-amplitude trade-off from model")
    ax_curve.set_xlabel("Unwrapped phase / pi")
    ax_curve.set_ylabel("Normalized amplitude |r| / mean(|r|)")
    ax_curve.set_ylim(-0.08, 3.55)
    ax_curve.legend(title="Photon energy", loc="upper right", frameon=True, facecolor="white", framealpha=0.88)
    _format_axis(ax_curve)
    _panel_label(ax_curve, "a")

    scatter = ax_span.scatter(
        phase_spans,
        amplitude_cv,
        c=energies,
        cmap="cividis",
        s=95,
        edgecolor="white",
        linewidth=0.8,
        zorder=3,
    )
    label_offsets = {
        1.665: (0.020, 0.010),
        1.680: (0.018, 0.014),
        result.params.design_energy_ev: (0.018, -0.018),
        1.710: (0.026, 0.030),
        1.725: (0.052, -0.035),
    }
    for energy, x_val, y_val in zip(energies, phase_spans, amplitude_cv, strict=True):
        dx, dy = label_offsets[float(energy)]
        ax_span.text(x_val + dx, y_val + dy, f"{energy:.3f}", fontsize=8, color=COLORS["ink"])
    design_index = int(np.argmin(np.abs(energies - result.params.design_energy_ev)))
    ax_span.scatter(
        [phase_spans[design_index]],
        [amplitude_cv[design_index]],
        s=170,
        facecolor="none",
        edgecolor=COLORS["red"],
        linewidth=1.4,
        zorder=4,
    )
    ax_span.axvspan(1.0, 1.5, color=COLORS["blue"], alpha=0.07, linewidth=0)
    ax_span.axhspan(0.0, 0.45, color=COLORS["teal"], alpha=0.07, linewidth=0)
    ax_span.text(
        0.04,
        0.94,
        "preferred window:\nlarge phase span,\nlower amplitude CV",
        transform=ax_span.transAxes,
        ha="left",
        va="top",
        color=COLORS["ink"],
    )
    ax_span.set_title("Operating-energy selection")
    ax_span.set_xlabel("Phase span (pi units)")
    ax_span.set_ylabel("Amplitude variation CV")
    ax_span.set_xlim(0.12, 1.48)
    ax_span.set_ylim(0.22, 1.08)
    cbar = fig.colorbar(scatter, ax=ax_span, pad=0.02)
    cbar.set_label("Photon energy (eV)")
    _format_axis(ax_span)
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
