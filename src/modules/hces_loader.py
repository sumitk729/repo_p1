import pandas as pd
from pathlib import Path

DATA_PATH = Path("data/raw/hces_2022_percapita_foodgrain.xlsx")


def load_raw_hces():
    """
    Load raw HCES 2022 per-capita foodgrain Excel data
    with two-level column headers:
    Level 0 -> Food item
    Level 1 -> Sector (Rural / Urban / Total)
    """
    df = pd.read_excel(
        DATA_PATH,
        header=[0, 1]
    )
    return df


def tidy_hces_foodgrain(df: pd.DataFrame) -> pd.DataFrame:
    """
    Convert raw HCES foodgrain data into tidy format:
    state | sector | food_item | per_capita_monthly_consumption
    """

    # Extract state names from the first column (MultiIndex)
    state_col = df.columns[0]
    states = df[state_col]

    # Drop the state column from the data
    df = df.drop(columns=[state_col])

    # Assign states as index
    df.index = states
    df.index.name = "state"

    # Drop rows where state is missing (safety)
    df = df[df.index.notna()]

    # Stack MultiIndex columns into tidy format
    tidy_df = (
        df
        .stack(level=0)   # food item
        .stack(level=0)   # sector
        .reset_index()
    )

    tidy_df.columns = [
        "state",
        "food_item",
        "sector",
        "per_capita_monthly_consumption",
    ]

    return tidy_df




