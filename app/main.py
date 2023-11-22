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
    age: int = 63
    sex: int = 1
    cp: int = 3
    trestbps: int = 145
    chol: int = 233
    fbs: int = 1
    restecg: int = 0
    thalach: int = 150
    exang: int = 0
    oldpeak: float = 2.3
    slope: int = 0
    ca: int = 0
    thal: int = 1

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
