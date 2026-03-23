from pydantic import BaseModel

class PassengerInput(BaseModel):
    Pclass: int
    Sex_male: int
    Age: float
    Fare: float
    FarePerPerson: float
    FamilySize: int
    Parch: int