import pandas as pd

def encode_features(df):
    # Convert categorical variables into numeric
    df = pd.get_dummies(df, drop_first=True)
    return df