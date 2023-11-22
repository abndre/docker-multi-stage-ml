# app/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

app = FastAPI()

# Carregar o modelo treinado
model_path = "../model/modelo_treinado.joblib"
loaded_model = joblib.load(model_path)

class Item(BaseModel):
    # Definir a estrutura da entrada da API (pode variar dependendo do seu caso)
    feature1: float
    feature2: float
    # Adicionar mais features conforme necessário

@app.post("/predict")
async def predict(item: Item):
    # Converter os dados de entrada em um DataFrame
    input_data = pd.DataFrame([item.dict()])

    # Fazer a predição
    prediction = loaded_model.predict(input_data)

    # Retornar o resultado da predição
    return {"prediction": int(prediction[0])}
