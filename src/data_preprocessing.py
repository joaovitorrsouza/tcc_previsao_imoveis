# src/data_preprocessing.py
import pandas as pd

def load_raw(path):
    return pd.read_csv(path)

def preprocess(df):
    df = df.copy()
    df["area_m2"] = df["area_m2"].astype(float)
    df = df.fillna({
        "quartos": df["quartos"].median(),
        "banheiros": df["banheiros"].median(),
        "vagas": df["vagas"].median()
    })
    df = pd.get_dummies(df, columns=["bairro"], prefix="bairro")
    return df
