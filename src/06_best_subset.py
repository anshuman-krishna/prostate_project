import pandas as pd
import itertools
import statsmodels.api as sm
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate_log.csv"

df = pd.read_csv(data_path)

y = df["lpsa"]
features = ["lvol", "lwht", "age", "lbh", "lpc"]

results = []

for k in range(1, len(features) + 1):
    for combo in itertools.combinations(features, k):
        x = df[list(combo)]
        x = sm.add_constant(x)
        model = sm.OLS(y, x).fit()
        results.append((combo, model.rsquared_adj))

results.sort(key=lambda x: x[1], reverse=True)

print(results[0])
