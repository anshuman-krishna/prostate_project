import pandas as pd
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate.csv"

df = pd.read_csv(data_path, sep=r"\s+")

print(df.shape)
print(df.isna().sum())
print(df.head())
