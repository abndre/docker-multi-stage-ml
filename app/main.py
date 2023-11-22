# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Carregar o modelo treinado e o encoder
model_path = "modelo_treinado.joblib"
encoder_path = "encoder.joblib"
loaded_model = joblib.load(model_path)
loaded_encoder = joblib.load(encoder_path)

class Item(BaseModel):
    age: int
    sex: int
    cp: int
    trestbps: int
    chol: int
    fbs: int
    restecg: int
    thalach: int
    exang: int
    oldpeak: float
    slope: int
    ca: int
    thal: int

@app.post("/predict")
async def predict(item: Item):
    # Criar um DataFrame com os novos dados
    new_data = pd.DataFrame([item.dict()])

    # Codificar variáveis categóricas usando o encoder treinado
    X_encoded = loaded_encoder.transform(new_data)

    # Fazer a predição
    prediction = loaded_model.predict(X_encoded)

    # Retornar o resultado da predição
    return {"prediction": int(prediction[0])}
