from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
from src.modules.indicators import (
    total_foodgrain_per_capita,
    pulses_per_capita,
    combined_foodgrain_pulses_table,
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
