import joblib
import pandas as pd
import json
import csv

from fastapi import FastAPI
from deployment.schema import PassengerInput

app = FastAPI()


model = joblib.load("models/best_model.pkl")


with open("features/feature_list.json", "r") as f:
    selected_features = json.load(f)["selected_features"]


@app.get("/")
def home():
    return {"message": "Titanic Survival Prediction API"}


@app.post("/predict")
def predict(data: PassengerInput):

  
    input_data = pd.DataFrame([data.dict()])

    
    input_data = input_data[selected_features]

   
    prediction = model.predict(input_data)[0]

    
    with open("logs/prediction_logs.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            data.Pclass,
            data.Sex_male,
            data.Age,
            data.Fare,
            data.FarePerPerson,
            data.FamilySize,
            data.Parch,
            prediction
        ])
    print(data)
    print(data.dict())

    result = "Survived" if prediction == 1 else "Not Survived"

    return {
        "prediction": int(prediction),
        "result": result
    }