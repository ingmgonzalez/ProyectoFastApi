from HeartData import Heart_data
# importar librerias necesarias 
import uvicorn
from fastapi import FastAPI
from HeartData import Heart_data
import numpy as np
import pickle
import pandas as pd

# Crear objeto de FastAPI 
app = FastAPI()

# Crear las rutasy funciones para los servicios 
@app.get('/')
def index():
    return {'Mensaje': 'Sistema de Clasificacion'}

# Crear ruta para prediccion
@app.post('/predecir')
def predecir(data: Heart_data):
    data = data.dict()
    
    Age = data['Age']
    Sex = data['Sex']
    Cp = data['Cp']
    Trestbps = data['Trestbps']
    Chol = data['Chol'] 
    Fbs = data['Fbs'] 
    Restecg = data['Restecg'] 
    Thalach = data['Thalach'] 
    Exang = data['Exang'] 
    Oldpeak = data['Age']
    Slope = data['Oldpeak'] 
    Ca = data['Ca'] 
    Thal = data['Thal'] 
    
    xin = np.array([Age, Sex, Cp, Trestbps, Chol, Fbs, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]).reshape(1,13)
    yout = model.predict(xin)
    mensaje = ''
    for y_out in yout:
        mensaje = mensaje + 'El paciente ' + labels[y_out] + ' tiene una enfermedad cardiaca\n'
    
    return mensaje
    
    

# Cargar modelo
pkl_filename = 'RF_heart_v2.pkl'
with open(pkl_filename, 'rb') as file:
    model = pickle.load(file)
    
labels = ['No', 'SI'] # Etiquetas de datos

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)