import pandas as pd
import numpy as np
import statsmodels.api as sm
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate_log.csv"

df = pd.read_csv(data_path)

y = df["lpsa"]
x = df[["lvol", "lwht", "age", "lpc"]]
x = sm.add_constant(x)

model = sm.OLS(y, x).fit()
print(model.summary())

new_patient = pd.DataFrame({
    "const": [1],
    "lvol": [np.log(7.2)],
    "lwht": [np.log(22)],
    "age": [67],
    "lpc": [np.log(0.26)]
})

pred_lpsa = model.predict(new_patient)[0]
pred_psa = np.exp(pred_lpsa)

print("predicted lpsa:", pred_lpsa)
print("predicted psa:", pred_psa)
