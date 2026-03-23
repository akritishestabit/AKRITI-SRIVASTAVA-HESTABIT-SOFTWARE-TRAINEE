import pandas as pd
import json
import os
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.neural_network import MLPClassifier

from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix

# -------------------------------
# 1️⃣ Load Data
# -------------------------------
print("Loading datasets...")

X_train = pd.read_csv("data/features/X_train.csv")
X_test = pd.read_csv("data/features/X_test.csv")
y_train = pd.read_csv("data/features/y_train.csv").values.ravel()
y_test = pd.read_csv("data/features/y_test.csv").values.ravel()

# -------------------------------
# 2️⃣ Load Selected Features
# -------------------------------
print("Loading selected features...")

with open("features/feature_list.json", "r") as f:
    selected_features = json.load(f)["selected_features"]

X_train = X_train[selected_features]
X_test = X_test[selected_features]

print("Selected Features:", selected_features)

# -------------------------------
# 3️⃣ Define Models
# -------------------------------
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000),
    "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
    "GradientBoosting": GradientBoostingClassifier(),
    "NeuralNetwork": MLPClassifier(hidden_layer_sizes=(64, 32), max_iter=500)
}

results = {}

# -------------------------------
# 4️⃣ Train + Cross Validation
# -------------------------------
print("\nTraining models with cross-validation...\n")

for name, model in models.items():
    print(f"Training {name}...")

    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring="accuracy")

    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    results[name] = {
        "cv_accuracy": cv_scores.mean(),
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_pred)
    }

    print(f"{name} done.\n")

# -------------------------------
# 5️⃣ Select Best Model
# -------------------------------
best_model_name = max(results, key=lambda x: results[x]["accuracy"])
best_model = models[best_model_name]

print("Best Model:", best_model_name)

# -------------------------------
# 6️⃣ Save Best Model
# -------------------------------
os.makedirs("models", exist_ok=True)

joblib.dump(best_model, "models/best_model.pkl")

print("Best model saved successfully!")

# -------------------------------
# 7️⃣ Save Metrics
# -------------------------------
os.makedirs("evaluation", exist_ok=True)

metrics_output = {
    "best_model": best_model_name,
    "metrics": results
}

with open("evaluation/metrics.json", "w") as f:
    json.dump(metrics_output, f, indent=4)

print("Metrics saved successfully!")

# -------------------------------
# 8️⃣ Confusion Matrix
# -------------------------------
import matplotlib.pyplot as plt
import seaborn as sns

y_pred_best = best_model.predict(X_test)

cm = confusion_matrix(y_test, y_pred_best)

plt.figure()
sns.heatmap(cm, annot=True, fmt="d")
plt.title(f"Confusion Matrix - {best_model_name}")
plt.xlabel("Predicted")
plt.ylabel("Actual")

plt.savefig("evaluation/confusion_matrix.png")

print("Confusion matrix saved!")