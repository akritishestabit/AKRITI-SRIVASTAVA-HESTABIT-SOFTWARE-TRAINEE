import pandas as pd
import json
import os
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier

print("Loading data...")

X_train = pd.read_csv("data/features/X_train.csv")
y_train = pd.read_csv("data/features/y_train.csv").values.ravel()


with open("features/feature_list.json", "r") as f:
    selected_features = json.load(f)["selected_features"]

X_train = X_train[selected_features]

print("Starting hyperparameter tuning...")


model = RandomForestClassifier(random_state=42)


param_grid = {
    "n_estimators": [50, 100, 200],
    "max_depth": [None, 5, 10],
    "min_samples_split": [2, 5]
}


grid_search = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid_search.fit(X_train, y_train)

print("Best Parameters:", grid_search.best_params_)
print("Best Score:", grid_search.best_score_)


os.makedirs("tuning", exist_ok=True)

results = {
    "best_params": grid_search.best_params_,
    "best_score": grid_search.best_score_
}

with open("tuning/results.json", "w") as f:
    json.dump(results, f, indent=4)

print("Tuning results saved!")