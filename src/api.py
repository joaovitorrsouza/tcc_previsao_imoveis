# src/api.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
from pathlib import Path

app = FastAPI(title="API de Previsão de Preços de Imóveis - RJ")

class Item(BaseModel):
    area_m2: float
    quartos: int
    banheiros: int
    vagas: int
    ano_construcao: int
    distancia_km_centro: float
    bairro: str

MODEL_PATH = Path("models/modelo_preco.pkl")
FEATURES_PATH = Path("models/modelo_preco_features.pkl")

if not MODEL_PATH.exists() or not FEATURES_PATH.exists():
    raise RuntimeError("Modelo ou features não encontrados. Rode o treinamento primeiro.")

model = joblib.load(MODEL_PATH)
model_features = joblib.load(FEATURES_PATH)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict")
def predict_endpoint(item: Item):
    payload = item.dict()
    try:
        from src.predict import predict as do_predict
        pred = do_predict(model, payload, model_features)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return {"preco_previsto": round(float(pred),2)}
