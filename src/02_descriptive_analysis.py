import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate.csv"

df = pd.read_csv(data_path, sep=r"\s+")

print(df.describe())

for col in df.columns:
    sns.boxplot(x=df[col])
    plt.title(col)
    plt.show()

for col in df.columns:
    if col != "psa":
        sns.scatterplot(x=df[col], y=df["psa"])
        plt.title(f"psa vs {col}")
        plt.show()
