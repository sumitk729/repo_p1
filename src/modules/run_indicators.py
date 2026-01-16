from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain
from src.modules.indicators import total_foodgrain_per_capita

df_tidy = tidy_hces_foodgrain(load_raw_hces())

FOODGRAINS = [
    "Rice",
    "Wheat",
    "Coarse Cereals",
]

df_indicator = total_foodgrain_per_capita(df_tidy, FOODGRAINS)

print(df_indicator.head(10))
print("\nRows:", len(df_indicator))
