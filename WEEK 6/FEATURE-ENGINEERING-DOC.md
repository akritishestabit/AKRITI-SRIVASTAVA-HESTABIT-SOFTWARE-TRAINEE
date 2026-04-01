# Feature Engineering Report (Day 2)

## Objective

To enhance model performance by creating meaningful features and selecting the most relevant ones.

---

## Feature Engineering

The following features were created:

* family_size: total family members
* is_alone: whether passenger is alone
* fare_per_person: fare divided by family size
* has_family: binary indicator of family presence
* age_group: categorical age segmentation
* fare_log: log transformation of fare
* age_fare_ratio: interaction between age and fare
* pclass_fare: interaction between class and fare
* age_squared: captures non-linearity
* fare_squared: captures non-linearity

---

## Encoding

* Applied One Hot Encoding on:

  * Sex
  * Embarked
  * age_group

---

## Feature Selection

* Used Mutual Information
* Removed low-importance features
* Retained only informative features

---

## Output

* X_train, X_test
* y_train, y_test
* feature_list.json

---

## Conclusion

The dataset is now transformed into a feature-rich and model-ready format.
