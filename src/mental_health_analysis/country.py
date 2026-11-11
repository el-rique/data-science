import pandas as pd


def country_treatment_rates(data: pd.DataFrame) -> pd.DataFrame:
    """Return treatment counts and response rates by country."""
    required_columns = {"Country", "treatment"}
    missing_columns = required_columns.difference(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {', '.join(sorted(missing_columns))}")

    unexpected_responses = set(data["treatment"].dropna().unique()).difference({"Yes", "No"})
    if unexpected_responses:
        values = ", ".join(sorted(map(str, unexpected_responses)))
        raise ValueError(f"Unexpected treatment responses: {values}")

    valid_responses = data.dropna(subset=["Country", "treatment"])
    counts = pd.crosstab(valid_responses["Country"], valid_responses["treatment"])
    counts = counts.reindex(columns=["Yes", "No"], fill_value=0)
    counts["total"] = counts["Yes"] + counts["No"]
    counts["treatment_rate_percent"] = counts["Yes"].div(counts["total"]).mul(100)
    return counts.sort_values("treatment_rate_percent", ascending=False)
