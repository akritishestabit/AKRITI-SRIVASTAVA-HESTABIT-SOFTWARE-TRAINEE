# Model Interpretation Report

## Overview

In this stage, the trained model was further analyzed to understand its behavior, improve performance, and identify its limitations. This included hyperparameter tuning, feature importance analysis, SHAP-based explainability, and error analysis.

The objective was not only to build a performant model but also to make it interpretable and reliable.

---

## Hyperparameter Tuning

Hyperparameter tuning was performed using GridSearchCV with stratified cross-validation. The model was optimized based on ROC-AUC to ensure good generalization.

### Best Parameters

* n_estimators: 100
* max_depth: 5
* min_samples_split: 2
* min_samples_leaf: 1

### Result

* Cross-validation ROC-AUC improved slightly after tuning
* The tuned model was more efficient and stable compared to the manually configured model

---

## Feature Importance Analysis

Feature importance was used to identify which features contributed most to model decisions.

### Key Observations

* Gender (encoded as `Sex_male`) was the most influential feature
* Passenger class (`Pclass`) had a strong impact on survival
* Fare and Age also contributed significantly
* Engineered features such as family size and fare-related transformations added value

This indicates that the model successfully captured meaningful real-world patterns.

---

## SHAP Analysis

SHAP (SHapley Additive exPlanations) was used to understand feature contributions at a deeper level.

### Key Insights

* Lower passenger class (Pclass = 3) negatively impacts survival
* Higher passenger class (Pclass = 1) positively impacts survival
* Younger passengers tend to have higher survival probability
* Higher age contributes negatively toward survival

SHAP helped in understanding not just which features are important, but how they influence predictions.

---

## Error Analysis

Error analysis was performed to identify where the model makes incorrect predictions.

### Observations

* Total errors: 32
* Majority of errors occurred in 3rd class passengers
* Average age of error cases was around 28 years
* Errors were more common among passengers with lower fare values
* Slightly higher errors were observed in male passengers

### Interpretation

The model struggles in cases where survival patterns are not clearly separable. For example:

* 3rd class passengers have mixed survival outcomes
* Young adult passengers do not follow a consistent survival pattern
* Some male passengers survived, creating ambiguity for the model

---

## Threshold Adjustment Impact

To improve recall, the classification threshold was adjusted from 0.5 to 0.4.

### Effect

* Recall improved significantly (more survivors detected)
* Some increase in false positives
* Error distribution slightly shifted, especially for borderline cases

This demonstrates the trade-off between precision and recall.

---

## Bias-Variance Understanding

* The model does not show signs of severe overfitting
* Cross-validation and test performance are consistent
* Errors are due to data ambiguity rather than model instability

---

## Conclusion

The final model demonstrates strong performance and reliable generalization. Through tuning and analysis, it was observed that:

* The model effectively captures key survival patterns
* Gender, class, and age are the most influential factors
* Errors primarily occur in ambiguous and overlapping cases
* Threshold tuning can be used to balance recall and precision

Overall, the model is both performant and interpretable, making it suitable for practical use and further improvement.

---
