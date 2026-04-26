import os
import pandas as pd
import numpy as np

RAW_DATA_PATH = "data/raw/titanic.csv"
PROCESSED_DATA_PATH = "data/processed/final.csv"


def load_data(path):
    print("Loading data...")
    df = pd.read_csv(path)
    return df


def remove_duplicates(df):
    print("Removing duplicates...")
    return df.drop_duplicates()


def drop_unnecessary_columns(df):
    print("Dropping unnecessary columns...")
    cols_to_drop = ["PassengerId", "Name", "Ticket", "Cabin"]
    df = df.drop(columns=cols_to_drop)
    return df


def handle_missing_values(df):
    print("Handling missing values...")

    
    df["Age"] = df["Age"].fillna(df["Age"].median())

   
    df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

    return df



def remove_outliers(df):
    print("Removing outliers using IQR...")

    
    col = "Fare"

    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    df = df[(df[col] >= lower) & (df[col] <= upper)]

    return df


def save_data(df, path):
    print("Saving processed data...")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)


def run_pipeline():
    df = load_data(RAW_DATA_PATH)

    df = remove_duplicates(df)
    df = drop_unnecessary_columns(df)
    df = handle_missing_values(df)
    df = remove_outliers(df)

    save_data(df, PROCESSED_DATA_PATH)

    print("Data pipeline completed successfully!")


if __name__ == "__main__":
    run_pipeline()