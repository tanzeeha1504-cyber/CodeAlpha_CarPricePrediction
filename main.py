from src.data_preprocessing import load_data, clean_data, save_data
from src.feature_engineering import encode_features
from src.train_model import train_model
from src.evaluate_model import evaluate

# Load data
df = load_data("data/raw/car_data.csv")

# Clean data
df = clean_data(df)

# Feature engineering
df = encode_features(df)

# Save processed data
save_data(df, "data/processed/clean_data.csv")

# Train model
model, X_test, y_test = train_model(df)

# Evaluate
evaluate(model, X_test, y_test)