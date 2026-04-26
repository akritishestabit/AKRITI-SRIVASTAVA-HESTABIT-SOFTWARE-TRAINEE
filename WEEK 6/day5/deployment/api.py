import os
import uuid
import joblib
import pandas as pd
import numpy as np
from datetime import datetime

from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()



MODEL_PATH = "models/best_model.pkl"
model = joblib.load(MODEL_PATH)



FEATURE_LIST = [
    "Pclass",
    "Age",
    "SibSp",
    "Parch",
    "Fare",
    "family_size",
    "is_alone",
    "fare_per_person",
    "has_family",
    "fare_log",
    "age_fare_ratio",
    "pclass_fare",
    "age_squared",
    "fare_squared",
    "Sex_male",
    "Embarked_Q",
    "Embarked_S",
    "age_group_teen",
    "age_group_young",
    "age_group_adult",
    "age_group_senior"
]



class PassengerInput(BaseModel):
    Age: float
    Fare: float
    Pclass: int
    Sex: str
    SibSp: int
    Parch: int
    Embarked: str



def generate_request_id():
    return str(uuid.uuid4())



def preprocess_input(data: PassengerInput):

    df = pd.DataFrame([data.dict()])

   
    df["family_size"] = df["SibSp"] + df["Parch"] + 1
    df["is_alone"] = (df["family_size"] == 1).astype(int)
    df["fare_per_person"] = df["Fare"] / df["family_size"]
    df["has_family"] = ((df["SibSp"] + df["Parch"]) > 0).astype(int)

  
    def get_age_group(age):
        if age <= 12:
            return "child"
        elif age <= 18:
            return "teen"
        elif age <= 35:
            return "young"
        elif age <= 60:
            return "adult"
        else:
            return "senior"

    df["age_group"] = df["Age"].apply(get_age_group)

    df["fare_log"] = np.log1p(df["Fare"])
    df["age_fare_ratio"] = df["Age"] / (df["Fare"] + 1)
    df["pclass_fare"] = df["Pclass"] * df["Fare"]
    df["age_squared"] = df["Age"] ** 2
    df["fare_squared"] = df["Fare"] ** 2

  
    df["Sex_male"] = (df["Sex"].str.lower() == "male").astype(int)

    df["Embarked_Q"] = (df["Embarked"] == "Q").astype(int)
    df["Embarked_S"] = (df["Embarked"] == "S").astype(int)

    df["age_group_teen"] = (df["age_group"] == "teen").astype(int)
    df["age_group_young"] = (df["age_group"] == "young").astype(int)
    df["age_group_adult"] = (df["age_group"] == "adult").astype(int)
    df["age_group_senior"] = (df["age_group"] == "senior").astype(int)

   
    df_final = df.reindex(columns=FEATURE_LIST, fill_value=0)

    return df_final



def log_prediction(request_id, input_data, prediction):

    log_data = {
    "request_id": request_id,
    "timestamp": datetime.now(),
    "prediction": int(prediction),
    **input_data   
}

    log_df = pd.DataFrame([log_data])

    log_file = "prediction_logs.csv"

    if not os.path.exists(log_file):
        log_df.to_csv(log_file, index=False)
    else:
        log_df.to_csv(log_file, mode="a", header=False, index=False)



@app.post("/predict")
def predict(data: PassengerInput):

    request_id = generate_request_id()

    
    processed_data = preprocess_input(data)

    
    prediction = model.predict(processed_data)[0]

   
    log_prediction(request_id, data.dict(), prediction)

    return {
        "request_id": request_id,
        "prediction": int(prediction)
    }