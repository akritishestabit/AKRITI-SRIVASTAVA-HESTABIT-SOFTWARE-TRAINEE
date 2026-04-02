
import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.metrics import confusion_matrix



def load_data():
    X_test = pd.read_csv("data/features/X_test.csv")
    y_test = pd.read_csv("data/features/y_test.csv").values.ravel()
    return X_test, y_test



def load_model():
    model = joblib.load("models/tuned_model.pkl")
    return model



def analyze_errors(model, X_test, y_test):

    print("Analyzing model errors...")

    y_pred = model.predict(X_test)

    
    df = X_test.copy()
    df["actual"] = y_test
    df["predicted"] = y_pred

   
    df["error"] = df["actual"] != df["predicted"]

   
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d")
    plt.title("Error Heatmap (Confusion Matrix)")
    plt.xlabel("Predicted")
    plt.ylabel("Actual")

    os.makedirs("evaluation", exist_ok=True)
    plt.savefig("evaluation/error_heatmap.png")
    plt.close()

    print("Error heatmap saved!")

  

    errors = df[df["error"] == True]

    print("\nTotal Errors:", len(errors))

  
    print("\nError Insights:")

    print("\nAvg Age (errors):", errors["Age"].mean() if "Age" in errors else "N/A")
    print("Avg Fare (errors):", errors["Fare"].mean() if "Fare" in errors else "N/A")

    if "Pclass" in errors:
        print("\nError distribution by Pclass:")
        print(errors["Pclass"].value_counts())

    if "Sex_male" in errors:
        print("\nError distribution by Gender (Sex_male):")
        print(errors["Sex_male"].value_counts())



def run_error_analysis():

    X_test, y_test = load_data()
    model = load_model()

    analyze_errors(model, X_test, y_test)


if __name__ == "__main__":
    run_error_analysis()

