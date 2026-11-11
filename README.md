# Mental Health Data Analysis

An exploratory analysis of a mental health survey dataset using Python.

## Project structure

```text
data/raw/                       Original survey dataset
src/mental_health_analysis/     Reusable analysis code and command-line interface
tests/                          Automated tests
outputs/                        Generated charts (not tracked by Git)
```

## Requirements

- Python 3.10 or newer
- Dependencies declared in `pyproject.toml`

Create and activate a virtual environment, then install the project from the repository root:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

Run all analyses:

```powershell
python -m mental_health_analysis --analysis all
```

Run one analysis by selecting `country`, `family-history`, `gender`, or `occupation`:

```powershell
python -m mental_health_analysis --analysis country
```

The gender chart is saved to `outputs/figures/gender_distribution.png`. The dataset path defaults to `data/raw/mental_health_dataset.csv`; use `--data` to provide another CSV.

Run the tests with:

```powershell
python -m unittest discover -s tests
```

## Data and interpretation

The included dataset is *Mental Health Dataset - Exploring the Landscape of Mental Well-being: A Comprehensive Dataset Analysis*, attributed to Bhavik Jikadara and published on Kaggle. Confirm the dataset's license and redistribution terms before republishing it.

The survey contains self-reported responses. Country-level treatment percentages describe only the records in this dataset; they should not be interpreted as population estimates or evidence of causation. The country analysis reports sample sizes alongside percentages and excludes rows without a country or a `Yes`/`No` treatment response rather than treating missing answers as `No`.
