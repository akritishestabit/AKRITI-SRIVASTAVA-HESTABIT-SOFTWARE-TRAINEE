
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


INPUT_PATH = "data/processed/final.csv"
OUTPUT_DIR = "data/features"

def load_data(path):
    print("Loading cleaned data...")
    return pd.read_csv(path)


def create_features(df):
    print("Creating new features...")

    # Family size
    df["family_size"] = df["SibSp"] + df["Parch"] + 1

    # is alone
    df["is_alone"] = (df["family_size"] == 1).astype(int)

    # fare per person
    df["fare_per_person"] = df["Fare"] / df["family_size"]

    # has family
    df["has_family"] = ((df["SibSp"] + df["Parch"]) > 0).astype(int)

    # age group
    df["age_group"] = pd.cut(
        df["Age"],
        bins=[0, 12, 18, 35, 60, 100],
        labels=["child", "teen", "young", "adult", "senior"]
    )

    # log transform of Fare
    df["fare_log"] = np.log1p(df["Fare"])

    # age-Fare ratio
    df["age_fare_ratio"] = df["Age"] / (df["Fare"] + 1)

    # pclass-Fare interaction
    df["pclass_fare"] = df["Pclass"] * df["Fare"]

    # age squared
    df["age_squared"] = df["Age"] ** 2

    # fare squared
    df["fare_squared"] = df["Fare"] ** 2

    return df


def encode_features(df):
    print("Encoding categorical features...")

    
    df = pd.get_dummies(df, columns=["Sex", "Embarked", "age_group"], drop_first=True)

    return df


def split_data(df):
    print("Splitting data...")

    X = df.drop("Survived", axis=1)
    y = df["Survived"]

    return train_test_split(X, y, test_size=0.2, random_state=42)


def save_data(X_train, X_test, y_train, y_test):
    print("Saving feature datasets...")

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    X_train.to_csv(f"{OUTPUT_DIR}/X_train.csv", index=False)
    X_test.to_csv(f"{OUTPUT_DIR}/X_test.csv", index=False)
    y_train.to_csv(f"{OUTPUT_DIR}/y_train.csv", index=False)
    y_test.to_csv(f"{OUTPUT_DIR}/y_test.csv", index=False)


def run_pipeline():
    df = load_data(INPUT_PATH)

    df = create_features(df)
    df = encode_features(df)

    X_train, X_test, y_train, y_test = split_data(df)

    save_data(X_train, X_test, y_train, y_test)

    print("Feature pipeline completed!")


if __name__ == "__main__":
    run_pipeline()

