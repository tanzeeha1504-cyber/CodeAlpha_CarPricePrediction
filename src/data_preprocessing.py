import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Drop unnecessary columns if present
    if 'Car_Name' in df.columns:
        df = df.drop('Car_Name', axis=1)

    # Handle missing values
    df = df.dropna()

    return df

def save_data(df, path):
    df.to_csv(path, index=False)