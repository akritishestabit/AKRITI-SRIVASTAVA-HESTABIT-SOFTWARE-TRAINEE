# Titanic Survival Prediction – End-to-End ML Pipeline

## Overview

This project implements a complete machine learning pipeline to predict passenger survival on the Titanic dataset.
It covers the full lifecycle of an ML system — from raw data analysis to deployment and monitoring.

The goal was not just to train a model, but to build a production-ready system that can be explained, deployed, and maintained.

---

## Project Structure

```
.
├── data/
│   ├── raw/
│   ├── processed/
│   └── features/
├── features/
│   ├── build_features.py
│   ├── feature_selector.py
│   └── feature_list.json
├── training/
│   ├── train.py
│   └── tuning.py
├── evaluation/
│   ├── metrics.json
│   ├── shap_analysis.py
│   └── error_evaluation.py
├── deployment/
│   ├── api.py
│   └── Dockerfile
├── monitoring/
│   └── drift_checker.py
├── models/
│   └── best_model.pkl
├── prediction_logs.csv
├── requirements.txt
└── README.md
```

---

## Week 6 Breakdown

### Day 1 – Data Cleaning & EDA

* Loaded raw Titanic dataset
* Removed duplicates and irrelevant columns
* Handled missing values:

  * Numerical → median
  * Categorical → mode
* Removed outliers using IQR method (on Fare)
* Performed EDA:

  * Correlation matrix
  * Feature distributions
  * Target distribution
  * Missing values heatmap

---

### Day 2 – Feature Engineering & Selection

* Created meaningful features:

  * family_size, is_alone, fare_per_person
  * age_group, fare_log, age_fare_ratio
  * pclass_fare, squared features
* Applied encoding:

  * One-hot encoding for categorical variables
* Performed feature selection using:

  * Mutual Information
* Saved final feature list

---

### Day 3 – Model Training

* Trained multiple models:

  * Logistic Regression
  * Random Forest
  * XGBoost
  * Neural Network
* Used 5-fold cross-validation
* Evaluated using:

  * Accuracy
  * Precision
  * Recall
  * F1 Score
  * ROC-AUC
* Selected best model based on cross-validated ROC-AUC
* Saved:

  * best_model.pkl
  * metrics.json
* Generated confusion matrix

---

### Day 4 – Tuning & Explainability

* Performed hyperparameter tuning (GridSearch/Random tuning)
* Improved model performance (especially recall)
* Generated:

  * Feature importance chart
  * SHAP summary plot
* Performed error analysis:

  * Error distribution by age, class, gender
* Identified where model makes mistakes

---

### Day 5 – Deployment & Monitoring

* Built API using FastAPI
* Created `/predict` endpoint
* Implemented:

  * Input validation using Pydantic
  * Feature engineering inside API
  * Prediction logging
  * Request ID tracking
* Stored predictions in `prediction_logs.csv`
* Implemented drift detection:

  * Compared training vs incoming data distributions
* Containerized project using Docker

---

## Model Details

* Final Model: Random Forest Classifier
* Selection based on cross-validated ROC-AUC
* Balanced performance across precision, recall, and stability

---

## API Usage

### Run API

```bash
uvicorn deployment.api:app --reload
```

### Endpoint

```
POST /predict
```

### Sample Input

```json
{
  "Age": 25,
  "Fare": 50,
  "Pclass": 1,
  "Sex": "female",
  "SibSp": 0,
  "Parch": 0,
  "Embarked": "S"
}
```

### Sample Output

```json
{
  "request_id": "unique-id",
  "prediction": 1
}
```

---

## Docker Deployment

### Build

```bash
docker build -t titanic-api -f deployment/Dockerfile .
```

### Run

```bash
docker run -p 8000:8000 titanic-api
```

---

## Monitoring

* Prediction logs stored in structured format
* Drift checker compares:

  * Training data distribution
  * Incoming prediction data
* Helps detect data drift and model degradation

---

## Key Learnings

* Importance of EDA before cleaning
* Feature engineering has major impact on performance
* Model selection should be based on validation metrics, not assumptions
* Deployment requires strict feature consistency
* Monitoring is essential after deployment

---

## Challenges Faced

* Feature mismatch between training and API
* Logging format initially incorrect for drift detection
* Docker build issues due to incorrect context
* Model recall improvement without hurting precision

---

## Future Improvements

* Add model versioning
* Deploy on cloud (AWS/GCP)
* Build real-time dashboard
* Automate retraining pipeline
* Use advanced drift detection methods

---

## Conclusion

This project demonstrates a complete ML pipeline with:

* Clean data processing
* Strong feature engineering
* Multi-model training
* Explainability and error analysis
* API deployment
* Monitoring and drift detection


