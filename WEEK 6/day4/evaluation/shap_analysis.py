
import os
import shap
import joblib
import pandas as pd
import matplotlib.pyplot as plt



def load_data():
    X_train = pd.read_csv("data/features/X_train.csv")
    return X_train



def load_model():
    model = joblib.load("models/tuned_model.pkl")
    return model



def plot_feature_importance(model, X_train):

    print("Generating feature importance...")

    importances = model.feature_importances_
    feature_names = X_train.columns

  
    df = pd.DataFrame({
        "feature": feature_names,
        "importance": importances
    }).sort_values(by="importance", ascending=False)

    # Plot
    plt.figure(figsize=(8, 5))
    plt.barh(df["feature"], df["importance"])
    plt.gca().invert_yaxis()
    plt.title("Feature Importance")

    plt.tight_layout()
    plt.savefig("evaluation/feature_importance.png")
    plt.close()

    print("Feature importance saved!")



def plot_shap(model, X_train):

    print("Generating SHAP summary plot...")

  
    explainer = shap.TreeExplainer(model)

    shap_values = explainer.shap_values(X_train)

   
    shap.summary_plot(shap_values, X_train, show=False)

    plt.savefig("evaluation/shap_summary.png")
    plt.close()

    print("SHAP summary saved!")


def run_analysis():

    os.makedirs("evaluation", exist_ok=True)

    X_train = load_data()
    model = load_model()

    plot_feature_importance(model, X_train)
    plot_shap(model, X_train)


if __name__ == "__main__":
    run_analysis()
