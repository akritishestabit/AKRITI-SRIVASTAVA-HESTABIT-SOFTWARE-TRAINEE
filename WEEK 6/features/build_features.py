import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

print("Loading dataset...")


df = pd.read_csv("data/processed/final.csv")

print("Dataset loaded successfully")


y = df["Survived"]



X = df.drop("Survived", axis=1)


X = X.drop(["Name", "Ticket", "Cabin", "PassengerId"], axis=1, errors="ignore")


print("Performing categorical encoding...")

X = pd.get_dummies(X, columns=["Sex", "Embarked"], drop_first=True)


print("Creating new features...")

X["FamilySize"] = df["SibSp"] + df["Parch"] + 1
X["IsAlone"] = (X["FamilySize"] == 1).astype(int)
X["FarePerPerson"] = df["Fare"] / X["FamilySize"]


print("Scaling numerical features...")

scaler = StandardScaler()

num_cols = ["Age", "Fare"]

X[num_cols] = scaler.fit_transform(X[num_cols])


print("Splitting dataset into train and test...")

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


os.makedirs("data/features", exist_ok=True)


print("Saving processed feature datasets...")

X_train.to_csv("data/features/X_train.csv", index=False)
X_test.to_csv("data/features/X_test.csv", index=False)

y_train.to_csv("data/features/y_train.csv", index=False)
y_test.to_csv("data/features/y_test.csv", index=False)

print("Feature engineering pipeline completed successfully!")