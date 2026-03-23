# Model Comparison Report

## Overview

In this step, multiple machine learning models were trained on the processed Titanic dataset to predict whether a passenger survived or not. The goal was to compare different models and select the best one based on performance.

The dataset used was already cleaned and transformed during previous steps. Only the most important features selected during feature engineering were used for training.

---

## Models Used

The following models were trained and evaluated:

1. Logistic Regression  
2. Random Forest  
3. Gradient Boosting  
4. Neural Network (MLP Classifier)

Each model was trained on the training dataset and evaluated using the test dataset.

---

## Evaluation Metrics

To compare the models, the following metrics were used:

- Accuracy: Measures overall correctness of the model  
- Precision: Measures how many predicted positives are actually correct  
- Recall: Measures how many actual positives were correctly predicted  
- F1 Score: Balance between precision and recall  
- ROC-AUC: Measures overall classification performance  

Cross-validation (5-fold) was also used to ensure the model is reliable and not overfitting.

---

## Results Summary

Each model produced different results based on how well it learned patterns from the data.

- Logistic Regression performed as a simple baseline model  
- Random Forest handled feature interactions better and improved performance  
- Gradient Boosting provided strong results by focusing on difficult cases  
- Neural Network captured complex patterns but required more iterations to converge  

After comparing all models, the best model was selected based on highest accuracy.

---

## Best Model

The best performing model was selected automatically based on test accuracy.

This model was saved as:

models/best_model.pkl

This saved model can be reused later for predictions or deployment.

---

## Confusion Matrix

A confusion matrix was generated for the best model to understand prediction behavior.

It shows:

- True Positives  
- True Negatives  
- False Positives  
- False Negatives  

This helps in understanding where the model is making mistakes.

The confusion matrix is saved at:

evaluation/confusion_matrix.png

---

## Conclusion

In this step, a complete training pipeline was built where multiple models were trained, evaluated, and compared.

The best model was selected automatically and saved for future use. This ensures that the system uses the most accurate model for predictions.

