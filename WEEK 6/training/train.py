
import os
import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import StratifiedKFold, cross_val_score

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from xgboost import XGBClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)



def load_data():
    X_train = pd.read_csv("data/features/X_train.csv")
    X_test = pd.read_csv("data/features/X_test.csv")
    y_train = pd.read_csv("data/features/y_train.csv").values.ravel()
    y_test = pd.read_csv("data/features/y_test.csv").values.ravel()

    return X_train, X_test, y_train, y_test



def get_models():
    return {

        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=1000))
        ]),

        "Random Forest": RandomForestClassifier(
            n_estimators=200,
            max_depth=5,
            random_state=42,
            class_weight="balanced"
        ),

        "XGBoost": XGBClassifier(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=4,
            eval_metric="auc",
            random_state=42
        ),

        "Neural Network": Pipeline([
            ("scaler", StandardScaler()),
            ("model", MLPClassifier(
                hidden_layer_sizes=(64, 32),
                max_iter=500,
                random_state=42
            ))
        ])
    }



def evaluate_model(model, X_train, y_train, X_test, y_test):

    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

   
    cv_score = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="roc_auc"
    ).mean()

   
    model.fit(X_train, y_train)

 
    # y_pred = model.predict(X_test)
    y_prob = model.predict_proba(X_test)[:, 1]
    y_pred = (y_prob >= 0.4).astype(int)
   

    
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred),
        "recall": recall_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred),
        "roc_auc": roc_auc_score(y_test, y_prob),
        "cv_roc_auc": cv_score
    }

    return metrics, model



def run_training():

    X_train, X_test, y_train, y_test = load_data()
    models = get_models()

    best_model = None
    best_score = -1
    best_name = ""
    all_metrics = {}

    for name, model in models.items():
        print(f"\nTraining {name}...")

        metrics, trained_model = evaluate_model(
            model, X_train, y_train, X_test, y_test
        )

        print(metrics)

        all_metrics[name] = metrics

       
        if metrics["cv_roc_auc"] > best_score:
            best_score = metrics["cv_roc_auc"]
            best_model = trained_model
            best_name = name

    
    

    cm = confusion_matrix(y_test, best_model.predict(X_test))

    plt.figure(figsize=(5, 4))
    plt.imshow(cm)
    plt.title(f"Confusion Matrix ({best_name})")
    plt.colorbar()

    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    
    for i in range(len(cm)):
        for j in range(len(cm[0])):
            plt.text(j, i, cm[i][j], ha="center", va="center")

    plt.tight_layout()

   
    plt.savefig("evaluation/confusion_matrix.png")
    plt.close()

    print("\nConfusion Matrix saved as evaluation/confusion_matrix.png")
    
    os.makedirs("models", exist_ok=True)
    os.makedirs("evaluation", exist_ok=True)

    joblib.dump(best_model, "models/best_model.pkl")

    with open("evaluation/metrics.json", "w") as f:
        json.dump(all_metrics, f, indent=4)

    print("\nBest Model:", best_name)
    print("Best CV ROC-AUC:", best_score)

    print(X_train.columns.tolist())

    


if __name__ == "__main__":
    run_training()

