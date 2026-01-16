from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
from src.modules.indicators import total_foodgrain_per_capita


FOODGRAINS = ["Rice", "Wheat", "Coarse Cereals"]


def test_total_foodgrain_structure():
    df = total_foodgrain_per_capita(
        tidy_hces_foodgrain(load_raw_hces()),
        FOODGRAINS,
    )

    assert set(df.columns) == {
        "state",
        "sector",
        "total_foodgrain_per_capita",
    }


def test_total_foodgrain_no_missing():
    df = total_foodgrain_per_capita(
        tidy_hces_foodgrain(load_raw_hces()),
        FOODGRAINS,
    )

    assert df["total_foodgrain_per_capita"].notna().all()


def test_total_foodgrain_positive():
    df = total_foodgrain_per_capita(
        tidy_hces_foodgrain(load_raw_hces()),
        FOODGRAINS,
    )

    assert (df["total_foodgrain_per_capita"] >= 0).all()

from src.modules.indicators import pulses_per_capita


def test_pulses_indicator_structure():
    df = pulses_per_capita(
        tidy_hces_foodgrain(load_raw_hces())
    )

    assert set(df.columns) == {
        "state",
        "sector",
        "pulses_per_capita",
    }


def test_pulses_indicator_no_missing():
    df = pulses_per_capita(
        tidy_hces_foodgrain(load_raw_hces())
    )

    assert df["pulses_per_capita"].notna().all()


def test_pulses_indicator_positive():
    df = pulses_per_capita(
        tidy_hces_foodgrain(load_raw_hces())
    )

    assert (df["pulses_per_capita"] >= 0).all()

from src.modules.indicators import combined_foodgrain_pulses_table


def test_combined_table_structure():
    df = combined_foodgrain_pulses_table(
        total_foodgrain_per_capita(
            tidy_hces_foodgrain(load_raw_hces()),
            ["Rice", "Wheat", "Coarse Cereals"],
        ),
        pulses_per_capita(
            tidy_hces_foodgrain(load_raw_hces())
        ),
    )

    assert set(df.columns) == {
        "state",
        "sector",
        "total_foodgrain_per_capita",
        "pulses_per_capita",
    }


def test_combined_table_no_row_loss():
    df_foodgrain = total_foodgrain_per_capita(
        tidy_hces_foodgrain(load_raw_hces()),
        ["Rice", "Wheat", "Coarse Cereals"],
    )

    df_combined = combined_foodgrain_pulses_table(
        df_foodgrain,
        pulses_per_capita(
            tidy_hces_foodgrain(load_raw_hces())
        ),
    )

    assert len(df_combined) == len(df_foodgrain)
