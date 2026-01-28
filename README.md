# Prostate Cancer Data Analysis
PCA and Linear Regression

This project performs exploratory data analysis, Principal Component Analysis (PCA), and linear regression on a prostate cancer dataset. The objective is to understand which clinical factors influence the prostate-specific antigen (PSA) level and to build interpretable predictive models.

---

## Project Structure

prostate_project/
│
├── data/
│ ├── prostate.csv
│ └── prostate_log.csv
│
├── src/
│ ├── 01_load_and_check.py
│ ├── 02_descriptive_analysis.py
│ ├── 03_log_transform.py
│ ├── 04_pca.py
│ ├── 05_simple_regression.py
│ ├── 06_best_subset.py
│ └── 07_prediction.py
│
├── outputs/
└── requirements.txt

---

## Requirements

Python 3 is required to run this project.

All required Python packages are listed in the `requirements.txt` file.

---

## Installation

From the project root directory, install the dependencies:

```bash
pip install -r requirements.txt
```

If pip does not work, use:
```bash
python3 -m pip install -r requirements.txt
```

Dataset
The dataset is located in data/prostate.csv.

Important note:
The dataset is space separated rather than comma separated. All scripts handle this format explicitly.

How to Run the Project
All commands below must be executed from the project root directory.
```bash
cd prostate_project
```
Step 1: Load and Check the Data
This script loads the dataset, checks the number of observations and variables, and verifies that there are no missing values.

```bash
python3 src/01_load_and_check.py
```

Expected output includes:
Dataset dimensions
Missing value check
Preview of the data

Step 2: Descriptive Statistics and Visualization
This script computes descriptive statistics and generates boxplots and scatter plots for exploratory analysis.

```bash
python3 src/02_descriptive_analysis.py
```
These plots help identify skewness, outliers, and non linear relationships.

Step 3: Log Transformation
This script applies a logarithmic transformation to skewed variables and saves a transformed dataset.
Log transformed variables:
- vol
- wht
- bh
- pc
- psa
Age is intentionally left untransformed.

```bash
python3 src/03_log_transform.py
```

After execution, the following file is created:

```bash
data/prostate_log.csv
```

Step 4: Principal Component Analysis
This script performs PCA on standardized explanatory variables and produces:
- Proportion of variance explained plot
- Cumulative proportion of variance explained plot
- Correlation circle
- PCA biplot

```bash
python3 src/04_pca.py
```
The response variable PSA is excluded from PCA to avoid information leakage.

Step 5: Simple Linear Regression
This script computes correlations between the target variable and predictors, identifies the most correlated predictor, and fits a simple linear regression model.

```bash
python3 src/05_simple_regression.py
```

The model predicts log PSA using log cancer volume.

Step 6: Best Subset Selection
This script evaluates all combinations of predictors and selects the best multiple linear regression model using adjusted R².

```bash
python3 src/06_best_subset.py
```
This approach balances model performance and complexity.

Step 7: Final Prediction
This script fits the final regression model and predicts PSA for a new patient.

Steps performed:
- Log transformation of new patient inputs
- Prediction of log PSA
- Back transformation to PSA scale

```bash
python3 src/07_prediction.py
```

The predicted PSA value is displayed in the terminal.

Thankyou.
