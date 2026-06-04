"""Generate Origin-rendered figures from the deterministic simulation data."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import numpy as np
import pandas as pd

from model.pipeline import BeamSteeringResult, run_pipeline
from model.reflection import phase_gradient_for_angle


FIGURE_BASENAMES = (
    "origin_figure_1_strong_coupling_gate_tuning",
    "origin_figure_2_complex_reflection_coefficient",
    "origin_figure_3_inverse_gate_profile",
    "origin_figure_4_programmable_beam_steering",
    "origin_figure_5_phase_amplitude_tradeoff",
)

COLORS = {
    "ink": "#1f2933",
    "muted": "#667085",
    "blue": "#3b6fb6",
    "cyan": "#2a9bb5",
    "teal": "#2f8f83",
    "orange": "#c47a2c",
    "red": "#c94c4c",
    "purple": "#7b61b7",
    "gray": "#a8b0bb",
}


def _require_originpro():
    try:
        import originpro as op
    except ImportError as exc:
        raise RuntimeError(
            "originpro is not installed. Install OriginLab originpro or run on a machine with Origin."
        ) from exc
    return op


def _downsample_reflectance(result: BeamSteeringResult) -> pd.DataFrame:
    energy_idx = np.linspace(0, len(result.energy_ev) - 1, 120, dtype=int)
    gate_idx = np.linspace(0, len(result.gate_voltage_v) - 1, 100, dtype=int)
    normalized = result.reflectance / np.nanmax(result.reflectance)
    gate_grid, energy_grid = np.meshgrid(result.gate_voltage_v[gate_idx], result.energy_ev[energy_idx])
    return pd.DataFrame(
        {
            "gate_voltage_v": gate_grid.ravel(),
            "photon_energy_ev": energy_grid.ravel(),
            "normalized_reflectance": normalized[np.ix_(energy_idx, gate_idx)].ravel(),
        }
    )


def _figure_1_data(result: BeamSteeringResult) -> dict[str, pd.DataFrame]:
    normalized = result.reflectance / np.nanmax(result.reflectance)
    lower, upper = result.polariton_energies_ev
    lower_idx = int(np.argmin(np.abs(result.energy_ev - lower)))
    design_idx = int(np.argmin(np.abs(result.energy_ev - result.params.design_energy_ev)))
    upper_idx = int(np.argmin(np.abs(result.energy_ev - upper)))
    return {
        "reflectance_map": _downsample_reflectance(result),
        "spectral_slices": pd.DataFrame(
            {
                "gate_voltage_v": result.gate_voltage_v,
                f"lower_{result.energy_ev[lower_idx]:.3f}_ev": normalized[lower_idx, :],
                f"design_{result.energy_ev[design_idx]:.3f}_ev": normalized[design_idx, :],
                f"upper_{result.energy_ev[upper_idx]:.3f}_ev": normalized[upper_idx, :],
                "linewidth_mev": result.linewidth_ev * 1000.0,
            }
        ),
    }


def _figure_2_data(result: BeamSteeringResult) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "gate_voltage_v": result.gate_voltage_v,
            "reflection_real": result.design_reflection.real,
            "reflection_imag": result.design_reflection.imag,
            "amplitude_abs_r": result.design_amplitude,
            "phase_pi": np.unwrap(np.angle(result.design_reflection)) / np.pi,
        }
    )


def _figure_3_data(result: BeamSteeringResult) -> dict[str, pd.DataFrame]:
    pixel = np.arange(result.params.metapixel_count)
    voltage = {"metapixel_index": pixel}
    for target in result.target_angles_deg:
        voltage[f"voltage_{target:.0f}_deg"] = result.voltage_profiles_v[float(target)]

    target = float(result.target_angles_deg[-1])
    desired = phase_gradient_for_angle(result.positions_m, result.params.wavelength_m, target)
    return {
        "voltage_profiles": pd.DataFrame(voltage),
        "phase_quantization": pd.DataFrame(
            {
                "metapixel_index": pixel,
                "target_phase_pi": desired / np.pi,
                "gate_selected_phase_pi": result.phase_profiles_rad[target] / np.pi,
            }
        ),
    }


def _figure_4_data(result: BeamSteeringResult) -> dict[str, pd.DataFrame]:
    far_field = {"observation_angle_deg": result.far_field_angles_deg}
    for target in result.target_angles_deg:
        far_field[f"intensity_{target:.0f}_deg"] = result.far_field_intensity[float(target)]
    targets = result.target_angles_deg
    peaks = np.array([result.far_field_peak_deg[float(t)] for t in targets])
    return {
        "far_field": pd.DataFrame(far_field),
        "target_peak": pd.DataFrame(
            {
                "programmed_angle_deg": targets,
                "target_angle_deg": targets,
                "simulated_peak_deg": peaks,
            }
        ),
    }


def _figure_5_data(result: BeamSteeringResult) -> dict[str, pd.DataFrame]:
    energies = np.array([1.665, 1.680, result.params.design_energy_ev, 1.710, 1.725])
    curves: list[pd.DataFrame] = []
    summary_rows: list[dict[str, float]] = []
    for energy in energies:
        idx = int(np.argmin(np.abs(result.energy_ev - energy)))
        response = result.reflection[idx, :]
        amp = np.abs(response)
        phase_pi = np.unwrap(np.angle(response)) / np.pi
        resolved_energy = float(result.energy_ev[idx])
        curves.append(
            pd.DataFrame(
                {
                    "photon_energy_ev": resolved_energy,
                    "phase_pi": phase_pi,
                    "normalized_amplitude": amp / np.mean(amp),
                }
            )
        )
        summary_rows.append(
            {
                "photon_energy_ev": resolved_energy,
                "phase_span_pi": float(np.max(phase_pi) - np.min(phase_pi)),
                "amplitude_cv": float(np.std(amp) / np.mean(amp)),
            }
        )
    return {
        "tradeoff_curves": pd.concat(curves, ignore_index=True),
        "energy_summary": pd.DataFrame(summary_rows),
    }


def write_origin_source_data(result: BeamSteeringResult, source_dir: Path) -> dict[str, Path]:
    source_dir.mkdir(parents=True, exist_ok=True)
    tables = {
        "figure_1_reflectance_map": _figure_1_data(result)["reflectance_map"],
        "figure_1_spectral_slices": _figure_1_data(result)["spectral_slices"],
        "figure_2_complex_reflection": _figure_2_data(result),
        "figure_3_voltage_profiles": _figure_3_data(result)["voltage_profiles"],
        "figure_3_phase_quantization": _figure_3_data(result)["phase_quantization"],
        "figure_4_far_field": _figure_4_data(result)["far_field"],
        "figure_4_target_peak": _figure_4_data(result)["target_peak"],
        "figure_5_tradeoff_curves": _figure_5_data(result)["tradeoff_curves"],
        "figure_5_energy_summary": _figure_5_data(result)["energy_summary"],
    }
    written: dict[str, Path] = {}
    for name, table in tables.items():
        path = source_dir / f"{name}.csv"
        table.to_csv(path, index=False)
        written[name] = path
    return written


def _new_wks(op, name: str, df: pd.DataFrame):
    wks = op.new_sheet("w", lname=name)
    wks.from_df(df)
    return wks


def _plot_lines(gl, wks, x_col: int, y_cols: list[int], colors: list[str]) -> None:
    for y_col, color in zip(y_cols, colors, strict=True):
        plot = gl.add_plot(wks, colx=x_col, coly=y_col, type="l")
        plot.color = color
        try:
            plot.set_float("line.width", 2.2)
        except Exception:
            pass
    gl.rescale()


def _style_axis(
    gl,
    xlabel: str,
    ylabel: str,
    xlim: tuple[float, float] | None = None,
    ylim: tuple[float, float] | None = None,
) -> None:
    gl.rescale()
    gl.axis("x").title = xlabel
    gl.axis("y").title = ylabel
    if xlim:
        gl.set_xlim(*xlim)
    if ylim:
        gl.set_ylim(*ylim)


def _title(gl, text: str, x: float, y: float) -> None:
    label = gl.add_label(text, x, y)
    if label:
        label.color = COLORS["ink"]


def _save_graph(page, output_dir: Path, basename: str) -> list[Path]:
    paths = [output_dir / f"{basename}.png", output_dir / f"{basename}.pdf"]
    page.save_fig(str(paths[0].resolve()), type="png", width=1500)
    page.save_fig(str(paths[1].resolve()), type="pdf")
    return paths


def _make_origin_graphs(result: BeamSteeringResult, output_dir: Path) -> list[Path]:
    op = _require_originpro()
    op.new(asksave=False)
    output_dir.mkdir(parents=True, exist_ok=True)

    exported: list[Path] = []

    fig1 = _figure_1_data(result)
    f1_slices = fig1["spectral_slices"].rename(
        columns={
            fig1["spectral_slices"].columns[1]: "lower polariton",
            fig1["spectral_slices"].columns[2]: "design energy",
            fig1["spectral_slices"].columns[3]: "upper polariton",
        }
    )
    wks1 = _new_wks(op, "F1 spectral slices", f1_slices)
    g1 = op.new_graph(lname="Origin Figure 1")
    gl1 = g1[0]
    _plot_lines(gl1, wks1, 0, [1, 2, 3], [COLORS["gray"], COLORS["blue"], COLORS["red"]])
    _style_axis(gl1, "Gate voltage (V)", "Normalized reflectance", (-3, 3), (-0.05, 1.10))
    _title(gl1, "Strong-coupling spectral slices", -2.65, 1.05)
    exported.extend(_save_graph(g1, output_dir, FIGURE_BASENAMES[0]))

    wks2 = _new_wks(
        op,
        "F2 complex reflection",
        _figure_2_data(result).rename(columns={"reflection_imag": "trajectory"}),
    )
    g2 = op.new_graph(lname="Origin Figure 2")
    gl2 = g2[0]
    plot = gl2.add_plot(wks2, colx=1, coly=2, type="y")
    plot.color = COLORS["blue"]
    plot.symbol_size = 6
    try:
        plot.set_float("line.width", 2.0)
    except Exception:
        pass
    gl2.rescale()
    _style_axis(gl2, "Re(r)", "Im(r)", (-0.75, 1.50), (-0.15, 0.70))
    _title(gl2, "Complex reflection trajectory", -0.55, 0.58)
    exported.extend(_save_graph(g2, output_dir, FIGURE_BASENAMES[1]))

    fig3 = _figure_3_data(result)
    wks3 = _new_wks(
        op,
        "F3 voltage profiles",
        fig3["voltage_profiles"].rename(
            columns={
                "voltage_0_deg": "0 deg",
                "voltage_10_deg": "10 deg",
                "voltage_20_deg": "20 deg",
            }
        ),
    )
    g3 = op.new_graph(lname="Origin Figure 3")
    gl3 = g3[0]
    _plot_lines(gl3, wks3, 0, [1, 2, 3], [COLORS["ink"], COLORS["teal"], COLORS["orange"]])
    _style_axis(
        gl3,
        "Metapixel index",
        "Gate voltage (V)",
        (0, result.params.metapixel_count - 1),
        (-3.35, 3.35),
    )
    _title(gl3, "Inverse-designed voltage maps", 5, 3.12)
    exported.extend(_save_graph(g3, output_dir, FIGURE_BASENAMES[2]))

    fig4 = _figure_4_data(result)
    wks4 = _new_wks(
        op,
        "F4 far field",
        fig4["far_field"].rename(
            columns={
                "intensity_0_deg": "target 0 deg",
                "intensity_10_deg": "target 10 deg",
                "intensity_20_deg": "target 20 deg",
            }
        ),
    )
    g4 = op.new_graph(lname="Origin Figure 4")
    gl4 = g4[0]
    _plot_lines(gl4, wks4, 0, [1, 2, 3], [COLORS["ink"], COLORS["teal"], COLORS["orange"]])
    _style_axis(gl4, "Observation angle (deg)", "Normalized intensity", (-5, 30), (-0.04, 1.08))
    _title(gl4, "Electrically programmed far field", -4, 1.04)
    exported.extend(_save_graph(g4, output_dir, FIGURE_BASENAMES[3]))

    fig5 = _figure_5_data(result)
    wks5 = _new_wks(
        op,
        "F5 energy summary",
        fig5["energy_summary"].rename(columns={"amplitude_cv": "amplitude CV"}),
    )
    g5 = op.new_graph(lname="Origin Figure 5")
    gl5 = g5[0]
    plot = gl5.add_plot(wks5, colx=1, coly=2, type="s")
    plot.color = COLORS["blue"]
    plot.symbol_size = 10
    gl5.rescale()
    _style_axis(gl5, "Phase span (pi units)", "Amplitude variation CV", (0.15, 1.42), (0.20, 1.08))
    _title(gl5, "Operating-energy selection", 0.20, 1.02)
    exported.extend(_save_graph(g5, output_dir, FIGURE_BASENAMES[4]))

    project_path = output_dir / "test1_origin_figures.opju"
    op.save(str(project_path.resolve()))
    exported.append(project_path)
    op.exit()
    return exported


def generate_origin_figures(output_dir: str | Path) -> list[Path]:
    out = Path(output_dir)
    result = run_pipeline()
    write_origin_source_data(result, out / "source_data")
    return _make_origin_graphs(result, out)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output-dir",
        default=ROOT / "output" / "origin",
        type=Path,
        help="Directory for Origin-generated figures and source data.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    paths = generate_origin_figures(args.output_dir)
    print(f"Generated {len(paths)} Origin files in {Path(args.output_dir).resolve()}")
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
