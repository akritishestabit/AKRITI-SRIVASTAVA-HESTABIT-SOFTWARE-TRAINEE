import shap
import pandas as pd
import joblib
import json
import numpy as np
import matplotlib.pyplot as plt

print("Loading model...")

model = joblib.load("models/best_model.pkl")

X_test = pd.read_csv("data/features/X_test.csv")

# Load selected features
with open("features/feature_list.json", "r") as f:
    selected_features = json.load(f)["selected_features"]

X_test = X_test[selected_features]

# -------------------------
# HARD FIX (important)
# -------------------------

# convert everything to float
X_test = X_test.apply(pd.to_numeric, errors='coerce')

# replace NaN
X_test = X_test.fillna(0)

# convert to numpy float
X_test = X_test.astype(float)

print("Data types after fix:")
print(X_test.dtypes)

print("Running SHAP analysis...")

# Use TreeExplainer explicitly (important)
explainer = shap.TreeExplainer(model)

shap_values = explainer.shap_values(X_test)

# Plot
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("evaluation/shap_summary.png")

print("SHAP summary plot saved!")