from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
from src.modules.indicators import (
    total_foodgrain_per_capita,
    pulses_per_capita,
)

df_tidy = tidy_hces_foodgrain(load_raw_hces())

FOODGRAINS = [
    "Rice",
    "Wheat",
    "Coarse Cereals",
]

df_foodgrain = total_foodgrain_per_capita(df_tidy, FOODGRAINS)
df_pulses = pulses_per_capita(df_tidy)

print("Foodgrains:")
print(df_foodgrain.head(5))

print("\nPulses:")
print(df_pulses.head(5))
