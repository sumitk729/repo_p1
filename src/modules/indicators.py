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
