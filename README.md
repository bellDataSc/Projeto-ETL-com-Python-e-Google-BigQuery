# Projeto ETL com Python e Google BigQuery

Este projeto realiza a extração de dados de uma API pública, transformação com Python/pandas e carga dos dados no Google BigQuery.

## Tecnologias
- Python 3.10+
- Pandas
- Requests
- Google Cloud BigQuery (via `google-cloud-bigquery`)

## Etapas do ETL

1. **Extração:** Coleta dados da API do IBGE.
2. **Transformação:** Normalização e limpeza dos dados JSON.
3. **Carga:** Envio dos dados para um dataset no BigQuery.

## Como rodar

```bash
# Instale dependências
pip install -r requirements.txt

# Execute a pipeline
python main.py
