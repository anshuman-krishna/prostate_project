import pandas as pd
import statsmodels.api as sm
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate_log.csv"

df = pd.read_csv(data_path)

corr = df.corr()["lpsa"].sort_values(ascending=False)
print(corr)

x = df["lvol"]
y = df["lpsa"]

x = sm.add_constant(x)

model = sm.OLS(y, x).fit()
print(model.summary())
