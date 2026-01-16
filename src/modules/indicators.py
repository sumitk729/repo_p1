import pandas as pd


def total_foodgrain_per_capita(
    df_tidy: pd.DataFrame,
    food_items: list[str],
) -> pd.DataFrame:
    """
    Compute total per-capita monthly foodgrain consumption.

    Parameters
    ----------
    df_tidy : DataFrame
        Output of tidy_hces_foodgrain
    food_items : list of str
        Food items to include in total

    Returns
    -------
    DataFrame with columns:
    state | sector | total_foodgrain_per_capita
    """

    df_filtered = df_tidy[df_tidy["food_item"].isin(food_items)]

    result = (
        df_filtered
        .groupby(["state", "sector"], as_index=False)
        ["per_capita_monthly_consumption"]
        .sum()
        .rename(columns={
            "per_capita_monthly_consumption": "total_foodgrain_per_capita"
        })
    )

    return result

def pulses_per_capita(
    df_tidy: pd.DataFrame,
) -> pd.DataFrame:
    """
    Compute per-capita monthly pulses consumption.

    Returns
    -------
    DataFrame with columns:
    state | sector | pulses_per_capita
    """

    df_pulses = df_tidy[df_tidy["food_item"] == "Pulses"]

    result = (
        df_pulses
        .groupby(["state", "sector"], as_index=False)
        ["per_capita_monthly_consumption"]
        .sum()
        .rename(columns={
            "per_capita_monthly_consumption": "pulses_per_capita"
        })
    )

    return result

def combined_foodgrain_pulses_table(
    df_foodgrain: pd.DataFrame,
    df_pulses: pd.DataFrame,
) -> pd.DataFrame:
    """
    Combine foodgrain and pulses indicators into a single table.

    Returns
    -------
    DataFrame with columns:
    state | sector | total_foodgrain_per_capita | pulses_per_capita
    """

    combined = df_foodgrain.merge(
        df_pulses,
        on=["state", "sector"],
        how="left",
    )

    return combined

def rank_states(
    df: pd.DataFrame,
    value_col: str,
    sector: str,
    ascending: bool = False,
) -> pd.DataFrame:
    """
    Rank states by a given indicator within a sector.

    Parameters
    ----------
    df : DataFrame
        Combined indicator table
    value_col : str
        Column to rank by
    sector : str
        'Rural' or 'Urban'
    ascending : bool
        False = highest first

    Returns
    -------
    Ranked DataFrame
    """

    ranked = (
        df[df["sector"] == sector]
        .sort_values(value_col, ascending=ascending)
        .assign(rank=lambda x: range(1, len(x) + 1))
    )

    return ranked[["rank", "state", "sector", value_col]]
