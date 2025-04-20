
import pandas as pd

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path)
    df.fillna(df.mean(), inplace=True)
    df['Chloramines'] = pd.to_numeric(df['Chloramines'], errors='coerce')
    df = df[df['Chloramines'].notnull()]
    return df
