# Data Report 

## Dataset Overview

For this exercise we used the Titanic dataset to understand passenger information and survival patterns.

The dataset contains 899 rows and 12 columns.  
Each row represents a passenger on the Titanic ship.

The main target column in this dataset is **Survived**.

Survived = 0 → Passenger did not survive  
Survived = 1 → Passenger survived


## Important Features

Some important columns used in this dataset are:

- Survived → Target variable
- Pclass → Passenger class (1st, 2nd, 3rd)
- Sex → Gender of passenger
- Age → Age of passenger
- Fare → Ticket price
- Embarked → Port from where passenger boarded


## Missing Values Analysis

From the data analysis we observed the following missing values:

- Age column has 177 missing values
- Cabin column has 695 missing values
- Embarked column has 2 missing values

The Cabin column has a large number of missing values compared to other columns.


## Exploratory Data Analysis Observations

### Survival Distribution
Most passengers did not survive the Titanic disaster.  
The number of passengers who died is higher than the number of passengers who survived.

### Gender vs Survival
Gender has a strong impact on survival.

- Around 74% of female passengers survived
- Around 18% of male passengers survived

This shows that female passengers had a much higher survival rate.

### Passenger Class vs Survival
Passenger class also affects survival.

Passengers in first class had higher survival chances compared to passengers in third class.

### Age Distribution
Most passengers were between 20 and 40 years old.

### Correlation Insights
From the correlation matrix we observed:

- Fare has a positive relation with survival
- Pclass has a negative relation with survival


## Conclusion

From the analysis we can see that the most important features affecting survival are:

- Sex
- Passenger class
- Age
- Fare

These features can be useful while building a machine learning model to predict survival.