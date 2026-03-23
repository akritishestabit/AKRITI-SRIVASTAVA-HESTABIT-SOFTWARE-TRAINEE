import pandas as pd


train_data = pd.read_csv("data/features/X_train.csv")


new_data = pd.read_csv("logs/prediction_logs.csv")


if "prediction" in new_data.columns:
    new_data = new_data.drop("prediction", axis=1)

print("Checking data drift...")

for col in train_data.columns:
    if col in new_data.columns:
        train_mean = train_data[col].mean()
        new_mean = new_data[col].mean()

        diff = abs(train_mean - new_mean)

        print(f"{col}: Train={train_mean:.2f}, New={new_mean:.2f}, Diff={diff:.2f}")

        if diff > 0.5:
            print(f"Warning: Data drift detected in {col}")