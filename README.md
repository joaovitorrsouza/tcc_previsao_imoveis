Projeto base - Previsão de preços de imóveis (RJ)

Como rodar o programa:
1) criar venv:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate

2) instalar:
   pip install -r requirements.txt

3) gerar dados:
   python scripts/generate_data.py

4) treinar:
   python src/train_model.py data/processed/exemplo_dados_rj_processed.csv models/modelo_preco.pkl

5) iniciar API:
   uvicorn src.api:app --reload --port 8000

Exemplo POST /predict payload JSON:
{
  "area_m2": 80,
  "quartos": 2,
  "banheiros": 1,
  "vagas": 1,
  "ano_construcao": 1995,
  "distancia_km_centro": 6.2,
  "bairro": "Botafogo"
}
curl -X POST "http://127.0.0.1:8000/predict" ^
-H "Content-Type: application/json" ^
-d "{\"area_m2\":80,\"quartos\":2,\"banheiros\":1,\"vagas\":1,\"ano_construcao\":1995,\"distancia_km_centro\":6.2,\"bairro\":\"Botafogo\"}"
