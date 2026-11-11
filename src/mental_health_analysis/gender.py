from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def gender_distribution(data: pd.DataFrame) -> pd.Series:
    """Count survey responses by gender, including missing values."""
    if "Gender" not in data.columns:
        raise ValueError("Missing required column: Gender")
    return data["Gender"].value_counts(dropna=False)


def save_gender_distribution(
    data: pd.DataFrame, output_path: str | Path
) -> Path:
    """Save a gender count chart and return its path."""
    if "Gender" not in data.columns:
        raise ValueError("Missing required column: Gender")

    chart_path = Path(output_path)
    chart_path.parent.mkdir(parents=True, exist_ok=True)

    figure, axis = plt.subplots(figsize=(10, 6))
    sns.countplot(data=data, x="Gender", ax=axis)
    axis.set(title="Survey responses by gender", xlabel="Gender", ylabel="Responses")
    axis.tick_params(axis="x", labelrotation=45)
    figure.tight_layout()
    figure.savefig(chart_path, dpi=150)
    plt.close(figure)
    return chart_path
