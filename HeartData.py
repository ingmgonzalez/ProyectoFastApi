from pydantic import BaseModel

class Heart_data(BaseModel):
    Age: int
    Sex: int 
    Cp: int 
    Trestbps: int 
    Chol: int 
    Fbs: int 
    Restecg: int 
    Thalach: int 
    Exang: int 
    Oldpeak: float 
    Slope: int 
    Ca: int 
    Thal: int 
    