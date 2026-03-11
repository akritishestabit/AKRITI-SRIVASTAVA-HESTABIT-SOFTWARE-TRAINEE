import pandas as pd
import json
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_classif


X_train = pd.read_csv("data/features/X_train.csv")
y_train = pd.read_csv("data/features/y_train.csv")


scores = mutual_info_classif(X_train, y_train.values.ravel())

feature_scores = pd.Series(scores, index=X_train.columns)

print(feature_scores.sort_values(ascending=False))


feature_scores.sort_values().plot(kind="barh")
plt.title("Feature Importance")
plt.show()


top_features = feature_scores.sort_values(ascending=False).head(6).index.tolist()

print("Selected Features:", top_features)


feature_data = {"selected_features": top_features}

with open("features/feature_list.json", "w") as f:
    json.dump(feature_data, f, indent=4)