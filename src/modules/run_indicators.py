from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
from src.modules.indicators import (
    total_foodgrain_per_capita,
    pulses_per_capita,
    combined_foodgrain_pulses_table,
    rank_states
)

df_tidy = tidy_hces_foodgrain(load_raw_hces())

FOODGRAINS = [
    "Rice",
    "Wheat",
    "Coarse Cereals",
]

df_foodgrain = total_foodgrain_per_capita(df_tidy, FOODGRAINS)
df_pulses = pulses_per_capita(df_tidy)

df_combined = combined_foodgrain_pulses_table(
    df_foodgrain,
    df_pulses,
)

print(df_combined.head(10))
print("\nColumns:", df_combined.columns.tolist())
print("Rows:", len(df_combined))


print("\nTop 5 states – Foodgrains (Rural)")
print(
    rank_states(
        df_combined,
        value_col="total_foodgrain_per_capita",
        sector="Rural",
    ).head(5)
)

print("\nTop 5 states – Pulses (Urban)")
print(
    rank_states(
        df_combined,
        value_col="pulses_per_capita",
        sector="Urban",
    ).head(5)
)


from pathlib import Path

OUTPUT_DIR = Path("data/outputs")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df_combined.to_csv(
    OUTPUT_DIR / "hces_2022_foodgrain_pulses_percapita.csv",
    index=False,
)

df_combined.to_parquet(
    OUTPUT_DIR / "hces_2022_foodgrain_pulses_percapita.parquet",
    index=False,
)
