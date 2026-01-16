'''
import pandas as pd

FILE_PATH = "data/raw/hces_2022_percapita_foodgrain.xlsx"

'''
'''
def inspect():
    df = pd.read_excel(FILE_PATH)
    print("Shape:", df.shape)
    print("Columns:")
    print(df.columns.tolist())
    print("\nFirst 5 rows:")
    print(df.head())


if __name__ == "__main__":
    inspect()

'''
'''
df = pd.read_excel(FILE_PATH)

print("Shape:", df.shape)
print("\nColumns:")
for i, col in enumerate(df.columns):
    print(i, col)

print("\nFirst 15 rows:")
print(df.head(15))

print("\nLast 10 rows:")
print(df.tail(10))
'''

from src.modules.hces_loader import load_raw_hces

df = load_raw_hces()

print("Columns (MultiIndex):")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())
