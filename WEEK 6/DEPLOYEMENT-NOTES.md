# Deployment Notes

## Overview

This project implements an end-to-end Machine Learning pipeline for predicting Titanic passenger survival.
The model is deployed as a REST API using FastAPI and containerized using Docker for consistent and scalable deployment.

---

## Model Details

* Best Model: Random Forest Classifier
* Selection Criteria: Cross-validated ROC-AUC
* Features: Engineered + selected features (21 total)
* Pipeline Includes:

  * Data Cleaning
  * Feature Engineering
  * Feature Selection
  * Model Training
  * Evaluation

---

## API Deployment

### Framework Used

* FastAPI (high-performance, async API framework)

### Endpoint

**POST /predict**

#### Input Format

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

#### Output Format

```json
{
  "request_id": "unique-id",
  "prediction": 1
}
```

---

## Key Deployment Features

### 1. Input Validation

* Implemented using Pydantic
* Ensures correct data types and structure before prediction

### 2. Feature Consistency

* Same feature engineering logic used as training
* Ensures no mismatch between training and inference

### 3. Logging System

* Predictions stored in `prediction_logs.csv`
* Includes:

  * Request ID
  * Timestamp
  * Input features
  * Prediction

### 4. Request Tracking

* Each request assigned a unique UUID
* Helps in debugging and monitoring

---

## Monitoring

### Data Drift Detection

* Implemented using `drift_checker.py`
* Compares training data vs incoming prediction data
* Detects distribution shifts using statistical differences

### Accuracy Monitoring (Conceptual)

* Performance can degrade over time due to drift
* Requires periodic retraining

---

## Docker Deployment

### Build Image

```bash
docker build -t titanic-api -f deployment/Dockerfile .
```

### Run Container

```bash
docker run -p 8000:8000 titanic-api
```

### Access API

```
http://localhost:8000/docs
```

---

## Dependencies

Managed using `requirements.txt`:

* fastapi
* uvicorn
* pandas
* numpy
* scikit-learn
* joblib

---


## Conclusion

The system is fully production-ready with:

* Clean pipeline
* Reliable API
* Monitoring support
* Containerized deployment

This demonstrates a complete ML lifecycle from data processing to deployment and monitoring.
