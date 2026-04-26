# Data Analysis & Preprocessing Report (Day 1)

## Objective

To perform exploratory data analysis on the Titanic dataset, identify data quality issues, and build a preprocessing pipeline to prepare clean data for further modeling.

---

## 1. EDA (Before Cleaning)

### Dataset Summary

* Rows: 899
* Columns: 12

### Key Observations

**Missing Values**

* Age: ~20% missing
* Cabin: ~77% missing
* Embarked: very few missing

**Irrelevant Features**

* PassengerId: identifier, no predictive value
* Name: high cardinality text
* Ticket: unstructured values

**Outliers**

* Fare has extreme values (up to ~500), indicating strong skewness

**Target Variable**

* Survived is slightly imbalanced but acceptable

**Correlation**

* Pclass and Fare show stronger relationship with survival
* Age has weak direct correlation

---

## 2. Data Cleaning Decisions

**Dropped Columns**

* PassengerId
* Name
* Ticket
* Cabin (due to excessive missing values)

**Missing Value Handling**

* Age filled with median
* Embarked filled with mode

**Duplicates**

* Duplicate rows removed

**Outlier Treatment**

* Fare processed using IQR method to remove extreme values

---

## 3. Data Pipeline

Steps implemented:

1. Load raw data
2. Remove duplicates
3. Drop irrelevant columns
4. Handle missing values
5. Remove outliers
6. Save processed data

---

## 4. EDA (After Cleaning)

**Improvements**

* No missing values
* Extreme outliers removed
* Distribution more stable
* Correlation patterns clearer

**Feature Insights**

* Strong: Pclass, Fare
* Moderate: SibSp
* Weak: Age

---

## Conclusion

The dataset has been cleaned and is ready for feature engineering and model training. The pipeline ensures reproducibility and can be updated if new features are required.

