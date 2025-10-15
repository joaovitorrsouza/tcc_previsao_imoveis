import pandas as pd
import numpy as np
from pathlib import Path

out_raw = Path("data/raw")
out_proc = Path("data/processed")
out_raw.mkdir(parents=True, exist_ok=True)
out_proc.mkdir(parents=True, exist_ok=True)

np.random.seed(42)
n = 500
bairros = {
    "Copacabana":1.3,"Ipanema":1.4,"Leblon":1.55,"Botafogo":1.1,
    "Flamengo":1.05,"Tijuca":0.85,"Maracanã":0.75,"Barra da Tijuca":1.15,
    "Recreio":0.95,"Centro":0.8
}
rows = []
for i in range(n):
    bairro = np.random.choice(list(bairros.keys()))
    area = int(max(20, np.round(np.random.normal(75,30))))
    quartos = int(np.clip(np.random.poisson(2), 1, 6))
    banheiros = int(np.clip(np.random.poisson(1.5), 1, 4))
    vagas = int(np.clip(np.random.poisson(1), 0, 3))
    ano = int(np.random.choice(range(1950,2021)))
    distancia = round(abs(np.random.normal(8 if bairro in ["Copacabana","Ipanema","Leblon","Botafogo","Flamengo"] else 18,5)),1)
    base = 7000
    factor = bairros[bairro]
    age = 1 - (2025-ano)*0.001
    price = area*base*factor*age + quartos*20000 + vagas*15000 - distancia*800 + np.random.normal(0,40000)
    price = int(max(50000, price))
    rows.append({
        "id": i+1, "bairro":bairro, "area_m2":area, "quartos":quartos,
        "banheiros":banheiros, "vagas":vagas, "ano_construcao":ano,
        "distancia_km_centro":distancia, "preco":price
    })

df = pd.DataFrame(rows)
df.to_csv(out_raw/"exemplo_dados_rj.csv", index=False)
df.to_csv(out_proc/"exemplo_dados_rj_processed.csv", index=False)
print("Dados gerados em:", out_raw/"exemplo_dados_rj.csv")
