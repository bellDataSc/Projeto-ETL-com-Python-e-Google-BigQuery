import pandas as pd

def transform_data(json_data):
    df = pd.json_normalize(json_data)
    df.columns = df.columns.str.lower()
    return df
