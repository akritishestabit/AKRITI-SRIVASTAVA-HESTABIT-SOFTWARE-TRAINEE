import pandas as pd

TRAIN_DATA_PATH = "data/processed/final.csv"
NEW_DATA_PATH = "prediction_logs.csv"


def load_data():
    print("Loading data...")
    train_df = pd.read_csv(TRAIN_DATA_PATH)

    try:
        new_df = pd.read_csv(NEW_DATA_PATH)
    except:
        print("No prediction logs found!")
        return train_df, None

    return train_df, new_df


def check_drift(train_df, new_df):

    print("\nChecking data drift...\n")

 
    num_cols = train_df.select_dtypes(include=["int64", "float64"]).columns

    for col in num_cols:

        if col not in new_df.columns:
            continue

        train_mean = train_df[col].mean()
        new_mean = new_df[col].mean()

        diff = abs(train_mean - new_mean)

        print(f"{col}:")
        print(f"Train Mean = {train_mean:.2f}")
        print(f"New Mean   = {new_mean:.2f}")
        print(f"Difference = {diff:.2f}")

        if diff > 5:  
            print("Drift detected\n")
        else:
            print("✔ Stable\n")


def run_drift_check():

    train_df, new_df = load_data()

    if new_df is None:
        return

    check_drift(train_df, new_df)


if __name__ == "__main__":
    run_drift_check()