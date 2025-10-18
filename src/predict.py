# src/predict.py
import joblib
import pandas as pd

def load_model(path):
    model = joblib.load(path)
    return model

def load_model_features(path):
    return joblib.load(path)  # expects features saved as joblib list

def prepare_input(payload, model_features):
    df = pd.DataFrame([{
        "area_m2": payload.get("area_m2"),
        "quartos": payload.get("quartos"),
        "banheiros": payload.get("banheiros"),
        "vagas": payload.get("vagas"),
        "ano_construcao": payload.get("ano_construcao"),
        "distancia_km_centro": payload.get("distancia_km_centro")
    }])
    # adiciona dummies de bairro conforme features
    for f in model_features:
        if f.startswith("bairro_"):
            bairro_name = f.replace("bairro_","")
            df[f] = 1 if payload.get("bairro") == bairro_name else 0
    # garantir todas as colunas presentes
    for f in model_features:
        if f not in df.columns:
            df[f] = 0
    df = df[model_features]
    return df

def predict(model, payload, model_features):
    X = prepare_input(payload, model_features)
    pred = model.predict(X)[0]
    return float(pred)
