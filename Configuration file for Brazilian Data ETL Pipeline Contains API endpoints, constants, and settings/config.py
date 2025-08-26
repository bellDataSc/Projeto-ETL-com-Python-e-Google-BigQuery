"""
Configuration file for Brazilian Data ETL Pipeline
Contains API endpoints, constants, and settings
"""

# IBGE API Endpoints
IBGE_BASE_URL = "https://servicodados.ibge.gov.br/api/v1"

# API Endpoints
ENDPOINTS = {
    "states": f"{IBGE_BASE_URL}/localidades/estados",
    "municipalities": f"{IBGE_BASE_URL}/localidades/municipios",
    "regions": f"{IBGE_BASE_URL}/localidades/regioes",
    "municipalities_by_state": f"{IBGE_BASE_URL}/localidades/estados/{{state_code}}/municipios"
}

# SIDRA API (for economic data)
SIDRA_BASE_URL = "https://apisidra.ibge.gov.br/values"

# Request settings
REQUEST_TIMEOUT = 30
MAX_RETRIES = 3

# Data processing settings
DEFAULT_ENCODING = "utf-8"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

# Visualization settings
DEFAULT_PLOT_HEIGHT = 500
DEFAULT_COLOR_PALETTE = "Set2"

# File export settings
EXPORT_FORMATS = ["csv", "excel", "json"]

# BigQuery settings (optional)
BIGQUERY_SETTINGS = {
    "project_id": "your-project-id",  # Update with your GCP project
    "dataset_id": "brazilian_data",
    "location": "US"
}

# Column mappings for data transformation
COLUMN_MAPPINGS = {
    "portuguese_to_english": {
        "nome": "name",
        "sigla": "code", 
        "regiao": "region",
        "populacao": "population",
        "area": "area",
        "densidade": "density"
    }
}

# State codes mapping
MAJOR_STATES = {
    "SP": "São Paulo",
    "MG": "Minas Gerais", 
    "RJ": "Rio de Janeiro",
    "BA": "Bahia",
    "PR": "Paraná",
    "RS": "Rio Grande do Sul",
    "PE": "Pernambuco",
    "CE": "Ceará",
    "PA": "Pará",
    "SC": "Santa Catarina"
}

# Regional codes
REGIONS = {
    1: "North",
    2: "Northeast", 
    3: "Southeast",
    4: "South",
    5: "Central-West"
}
