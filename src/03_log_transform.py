import pandas as pd
import numpy as np
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate.csv"
out_path = base_dir / "data" / "prostate_log.csv"

df = pd.read_csv(data_path, sep=r"\s+")

log_cols = ["vol", "wht", "bh", "pc", "psa"]

for col in log_cols:
    df["l" + col] = np.log(df[col])

df.to_csv(out_path, index=False)

print(df.head())
