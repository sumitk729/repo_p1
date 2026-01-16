from src.modules.hces_loader import load_raw_hces, tidy_hces_foodgrain

df_raw = load_raw_hces()
df_tidy = tidy_hces_foodgrain(df_raw)

print(df_tidy.head(10))
print("\nUnique sectors:", df_tidy["sector"].unique())
print("Unique food items:", df_tidy["food_item"].unique())
print("Number of states:", df_tidy["state"].nunique())
