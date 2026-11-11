import argparse
from collections.abc import Callable
from pathlib import Path

import pandas as pd

from mental_health_analysis.country import country_treatment_rates
from mental_health_analysis.data import DEFAULT_DATA_PATH, load_dataset
from mental_health_analysis.family_history import treatment_by_family_history
from mental_health_analysis.gender import gender_distribution, save_gender_distribution
from mental_health_analysis.occupation import treatment_by_occupation_and_stress


def _show_country_analysis(data: pd.DataFrame) -> None:
    rates = country_treatment_rates(data)
    display_columns = ["Yes", "No", "total", "treatment_rate_percent"]
    print("Countries with the highest treatment response rates:")
    print(rates[display_columns].head(10).to_string())
    print("\nCountries with the lowest treatment response rates:")
    print(rates[display_columns].tail(10).sort_values("treatment_rate_percent").to_string())


def _show_family_history_analysis(data: pd.DataFrame) -> None:
    print(treatment_by_family_history(data).to_string())


def _show_gender_analysis(data: pd.DataFrame) -> None:
    print("Responses by gender:")
    print(gender_distribution(data).to_string())
    chart_path = save_gender_distribution(
        data, DEFAULT_DATA_PATH.parents[2] / "outputs" / "figures" / "gender_distribution.png"
    )
    print(f"\nGender chart saved to: {chart_path}")


def _show_occupation_analysis(data: pd.DataFrame) -> None:
    print(treatment_by_occupation_and_stress(data).to_string())


ANALYSES: dict[str, Callable[[pd.DataFrame], None]] = {
    "country": _show_country_analysis,
    "family-history": _show_family_history_analysis,
    "gender": _show_gender_analysis,
    "occupation": _show_occupation_analysis,
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Explore a mental health survey dataset."
    )
    parser.add_argument(
        "--analysis",
        choices=["all", *ANALYSES],
        default="all",
        help="Analysis to run (default: all).",
    )
    parser.add_argument(
        "--data",
        type=Path,
        default=DEFAULT_DATA_PATH,
        help="Path to the survey CSV.",
    )
    return parser


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    data = load_dataset(args.data)
    selected_analyses = ANALYSES if args.analysis == "all" else {args.analysis: ANALYSES[args.analysis]}

    for name, analysis in selected_analyses.items():
        print(f"\n=== {name.replace('-', ' ').title()} ===")
        analysis(data)


if __name__ == "__main__":
    main()
