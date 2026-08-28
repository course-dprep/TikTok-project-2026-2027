from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file from a path."""
    return pd.read_csv(Path(path))


def dataset_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return common summary statistics for numeric columns."""
    return df.describe(include="number").transpose()


def missing_values(df: pd.DataFrame) -> pd.Series:
    """Return missing value counts per column."""
    return df.isna().sum().sort_values(ascending=False)
