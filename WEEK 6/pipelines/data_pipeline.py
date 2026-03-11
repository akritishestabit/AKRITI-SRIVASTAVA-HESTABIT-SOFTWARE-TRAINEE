import pandas as pd
import os

RAW_DATA_PATH = "data/raw/dataset.csv"
PROCESSED_DATA_PATH = "data/processed/final.csv"


def load_data():
    print("Loading dataset...")
    df = pd.read_csv(RAW_DATA_PATH)
    return df


def clean_data(df):
    print("Cleaning dataset...")

    # remove duplicates
    df = df.drop_duplicates()

    # fill missing values
    df = df.fillna(df.mean(numeric_only=True))

    return df


def save_data(df):
    print("Saving cleaned dataset...")
    os.makedirs("data/processed", exist_ok=True)
    df.to_csv(PROCESSED_DATA_PATH, index=False)


def main():
    df = load_data()
    df = clean_data(df)
    save_data(df)

    print("Data pipeline completed!")


if __name__ == "__main__":
    main()