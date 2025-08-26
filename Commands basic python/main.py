from src.extract import extract_data
from src.transform import transform_data
from src.load import load_to_bigquery

def run_pipeline():
    print("Extraindo dados...")
    data = extract_data()
    
    print("Transformando dados...")
    df = transform_data(data)
    
    print("Carregando dados no BigQuery...")
    load_to_bigquery(df)

if __name__ == "__main__":
    run_pipeline()
