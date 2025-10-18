# src/train_model.py
import pandas as pd
import joblib
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
import sys
from math import sqrt
def train(path_processed, model_out):
    df = pd.read_csv(path_processed)
    X = df[["area_m2","quartos","banheiros","vagas","ano_construcao","distancia_km_centro"]].copy()
    bairro_cols = [c for c in df.columns if c.startswith("bairro_")]
    if bairro_cols:
        X = pd.concat([X, df[bairro_cols]], axis=1)
    y = df["preco"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    mae = mean_absolute_error(y_test, preds)
    rmse = sqrt(mean_squared_error(y_test, preds))
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

    joblib.dump(model, model_out)
    # salvar lista de features
    joblib.dump(list(X.columns), model_out.replace(".pkl","_features.pkl"))

if __name__ == "__main__":
    # ex: python src/train_model.py data/processed/exemplo_dados_rj_processed.csv models/modelo_preco.pkl
    if len(sys.argv) != 3:
        print("Uso: python src/train_model.py <processed_csv> <modelo_saida.pkl>")
    else:
        train(sys.argv[1], sys.argv[2])
