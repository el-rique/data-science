import pandas as pd


def treatment_by_family_history(data: pd.DataFrame) -> pd.DataFrame:
    """Count treatment responses for each family-history response."""
    required_columns = {"family_history", "treatment"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing_columns))}")
    return pd.crosstab(data["family_history"], data["treatment"])
