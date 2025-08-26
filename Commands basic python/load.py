from google.cloud import bigquery
from src.config import GCP_PROJECT_ID, BQ_DATASET, BQ_TABLE

def load_to_bigquery(df):
    client = bigquery.Client(project=GCP_PROJECT_ID)
    table_id = f"{GCP_PROJECT_ID}.{BQ_DATASET}.{BQ_TABLE}"
    
    job = client.load_table_from_dataframe(df, table_id)
    job.result()
    print(f"Carregado {df.shape[0]} linhas para {table_id}")
