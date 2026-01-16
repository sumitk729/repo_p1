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
