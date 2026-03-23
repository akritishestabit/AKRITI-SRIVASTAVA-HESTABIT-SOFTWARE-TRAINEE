# Deployment Notes

This project is a complete machine learning pipeline for Titanic survival prediction.

First, data was cleaned and analyzed using EDA. Then feature engineering was applied to create meaningful features like FamilySize and FarePerPerson.

After that, multiple models were trained and the best model was selected using hyperparameter tuning.

The model was then deployed using FastAPI to create an API endpoint for predictions.

Docker was used to containerize the application so it can run consistently in any environment.

Prediction logs are stored in a CSV file and monitored for data drift using a drift checker script.

Overall, this project demonstrates end-to-end ML pipeline including data processing, model building, evaluation, deployment, and monitoring.