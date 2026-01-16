# Test 1: checking whether I can even load the Excel file.

from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
import pandas as pd


def test_load_raw_hces_returns_dataframe():
    df = load_raw_hces()
    assert isinstance(df, pd.DataFrame)
    assert not df.empty

# Test 2: Tidy output has requirred columns

def test_tidy_hces_has_expected_columns():
    df_raw = load_raw_hces()
    df_tidy = tidy_hces_foodgrain(df_raw)

    expected_columns = {
        "state",
        "sector",
        "food_item",
        "per_capita_monthly_consumption",
    }

    assert set(df_tidy.columns) == expected_columns

# Test 3 — Sector values are exactly what we expect

def test_tidy_hces_sector_values():
    df_raw = load_raw_hces()
    df_tidy = tidy_hces_foodgrain(df_raw)

    sectors = set(df_tidy["sector"].unique())
    assert sectors == {"Rural", "Urban", "Total"}

# Test 4 — No missing states or values
def test_tidy_hces_no_missing_keys():
    df_raw = load_raw_hces()
    df_tidy = tidy_hces_foodgrain(df_raw)

    assert df_tidy["state"].notna().all()
    assert df_tidy["food_item"].notna().all()
    assert df_tidy["per_capita_monthly_consumption"].notna().all()

# Test 5 — At least one known state exists (anchor test)

def test_known_state_exists():
    df_raw = load_raw_hces()
    df_tidy = tidy_hces_foodgrain(df_raw)

    assert "Uttar Pradesh" in set(df_tidy["state"])

