import pandas as pd


def treatment_by_occupation_and_stress(data: pd.DataFrame) -> pd.DataFrame:
    """Cross-tabulate occupation, treatment, and reported growing stress."""
    required_columns = {"Occupation", "treatment", "Growing_Stress"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing_columns))}")

    return pd.crosstab(
        index=[data["Occupation"], data["treatment"]],
        columns=data["Growing_Stress"],
        margins=True,
    )
