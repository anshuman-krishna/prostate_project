import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from pathlib import Path

base_dir = Path(__file__).resolve().parent.parent
data_path = base_dir / "data" / "prostate_log.csv"

df = pd.read_csv(data_path)

features = ["lvol", "lwht", "age", "lbh", "lpc"]
x = df[features]

x_scaled = StandardScaler().fit_transform(x)

# pca for pve
pca_full = PCA()
pca_full.fit(x_scaled)

pve = pca_full.explained_variance_ratio_
cum_pve = np.cumsum(pve)

# pve plot
plt.figure()
plt.plot(range(1, len(pve) + 1), pve, marker="o")
plt.xlabel("principal component")
plt.ylabel("proportion of variance explained")
plt.title("pve vs number of components")
plt.show()

# cumulative pve plot
plt.figure()
plt.plot(range(1, len(cum_pve) + 1), cum_pve, marker="o")
plt.xlabel("principal component")
plt.ylabel("cumulative proportion of variance explained")
plt.title("cumulative pve vs number of components")
plt.show()

# pca for biplot
pca_2 = PCA(n_components=2)
scores = pca_2.fit_transform(x_scaled)
loadings = pca_2.components_.T

# correlation circle
plt.figure()
for i, var in enumerate(features):
    plt.arrow(0, 0, loadings[i, 0], loadings[i, 1], head_width=0.05)
    plt.text(loadings[i, 0]*1.1, loadings[i, 1]*1.1, var)

circle = plt.Circle((0, 0), 1, fill=False)
plt.gca().add_artist(circle)

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("correlation circle")
plt.axis("equal")
plt.show()

# biplot
plt.figure()
plt.scatter(scores[:, 0], scores[:, 1], alpha=0.5)

for i, var in enumerate(features):
    plt.arrow(
        0, 0,
        loadings[i, 0] * max(scores[:, 0]),
        loadings[i, 1] * max(scores[:, 1]),
        head_width=0.1
    )
    plt.text(
        loadings[i, 0] * max(scores[:, 0]) * 1.1,
        loadings[i, 1] * max(scores[:, 1]) * 1.1,
        var
    )

plt.xlabel("PC1")
plt.ylabel("PC2")
plt.title("pca biplot")
plt.show()
