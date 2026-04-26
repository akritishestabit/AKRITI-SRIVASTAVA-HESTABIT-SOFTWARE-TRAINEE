
import pandas as pd
from sklearn.feature_selection import mutual_info_classif
import json

INPUT_PATH = "data/features/X_train.csv"
TARGET_PATH = "data/features/y_train.csv"
OUTPUT_PATH = "features/feature_list.json"


def load_data():
    X = pd.read_csv(INPUT_PATH)
    y = pd.read_csv(TARGET_PATH)
    return X, y.values.ravel()


def select_features(X, y):
    print("Calculating feature importance...")

    mi_scores = mutual_info_classif(X, y)

    feature_scores = pd.Series(mi_scores, index=X.columns)
    feature_scores = feature_scores.sort_values(ascending=False)

    
    selected_features = feature_scores[feature_scores > 0.01].index.tolist()

    print("Selected features:", selected_features)

    return selected_features


def save_features(features):
    with open(OUTPUT_PATH, "w") as f:
        json.dump(features, f)

    print("Feature list saved!")


def run():
    X, y = load_data()
    selected_features = select_features(X, y)
    save_features(selected_features)


if __name__ == "__main__":
    run()

