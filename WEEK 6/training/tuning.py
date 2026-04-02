
import json
import joblib
import pandas as pd

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier



def load_data():
    X_train = pd.read_csv("data/features/X_train.csv")
    y_train = pd.read_csv("data/features/y_train.csv").values.ravel()
    return X_train, y_train



def tune_model():

    X_train, y_train = load_data()

    
    model = RandomForestClassifier(random_state=42)

    
    param_grid = {
        "n_estimators": [100, 200, 300],
        "max_depth": [3, 5, 7],
        "min_samples_split": [2, 5],
        "min_samples_leaf": [1, 2]
    }

   
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    
    grid = GridSearchCV(
        estimator=model,
        param_grid=param_grid,
        cv=cv,
        scoring="roc_auc",
        n_jobs=-1,
        verbose=1
    )

    print("Starting hyperparameter tuning...")
    grid.fit(X_train, y_train)

    print("\nBest Parameters:", grid.best_params_)
    print("Best CV ROC-AUC:", grid.best_score_)

    return grid



def save_results(grid):

    
    joblib.dump(grid.best_estimator_, "models/tuned_model.pkl")

    
    results = {
        "best_params": grid.best_params_,
        "best_score": grid.best_score_
    }

    with open("tuning/results.json", "w") as f:
        json.dump(results, f, indent=4)

    print("\nTuned model and results saved!")



def run_tuning():

    grid = tune_model()
    save_results(grid)


if __name__ == "__main__":
    run_tuning()
