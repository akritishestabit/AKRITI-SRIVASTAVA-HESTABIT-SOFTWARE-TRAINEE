# Model Comparison Report

## Overview

In this project, multiple machine learning models were trained and evaluated on the Titanic dataset to predict passenger survival. The goal was to compare different algorithms and select the best model based on reliable evaluation metrics.

The models used were:

* Logistic Regression
* Random Forest
* XGBoost
* Neural Network

Evaluation was performed using both test metrics and cross-validation, with a primary focus on ROC-AUC for model selection.

---

## Evaluation Metrics Used

* Accuracy: Measures overall correctness
* Precision: Measures correctness of positive predictions
* Recall: Measures ability to detect actual positives
* F1 Score: Balance between precision and recall
* ROC-AUC: Measures overall model discrimination capability
* Cross-Validation ROC-AUC: Used for robust model selection

---

## Model Performance Summary

### Logistic Regression

* Performed well with balanced metrics
* Strong ROC-AUC indicates good separation capability
* Works well when relationships are relatively linear

### Random Forest

* Achieved the highest cross-validation ROC-AUC
* Demonstrated strong generalization ability
* Performed consistently across folds
* Handled non-linear patterns effectively

### XGBoost

* Showed competitive performance
* Slightly lower than Random Forest in this case
* Improved after tuning but did not outperform Random Forest
* More effective on larger or more complex datasets

### Neural Network

* Reasonable performance but slightly lower than other models
* Training did not fully converge
* Requires more data and tuning for optimal performance

---

## Model Selection Strategy

The best model was selected based on cross-validation ROC-AUC rather than test accuracy. This ensures that the selected model generalizes well to unseen data and is not overfitting.

Random Forest achieved the highest cross-validation ROC-AUC, making it the most reliable model for this dataset.

---

## Confusion Matrix Insight

The confusion matrix showed:

* Low false positives
* Higher false negatives

This indicates that the model is conservative in predicting survival. It tends to predict "not survived" more often, resulting in higher precision but relatively lower recall.

---

## Key Observations

* Model performance depends heavily on feature engineering and preprocessing
* Simpler models like Random Forest can outperform complex models on smaller datasets
* XGBoost benefits more from larger datasets and deeper feature engineering
* Cross-validation provides a more reliable estimate than a single test split

---

## Conclusion

Random Forest was selected as the best model because it achieved the highest cross-validation ROC-AUC and demonstrated stable performance across different folds.


