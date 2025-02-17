# model_training.py
import pandas as pd
import os
import json

def train_model():
    # Path to one dataset file (adjust as needed).
    file_path = os.path.join("dataset", "bid.06.txt")
    
    if not os.path.exists(file_path):
        print("Dataset file not found:", file_path)
        return

    # The dataset is tab-separated with no header.
    # According to the problem statement, column 18 (0-indexed column 17) is adSlotFloorPrice.
    try:
        # Read only the adSlotFloorPrice column from the first 100,000 rows for speed.
        df = pd.read_csv(file_path, sep="\t", header=None, usecols=[17], nrows=100000)
    except Exception as e:
        print("Error reading file:", e)
        return

    # Convert the values to numeric; coerce errors to NaN and drop them.
    df[17] = pd.to_numeric(df[17], errors="coerce")
    df = df.dropna()

    if df.empty:
        print("No valid floor price data found.")
        return

    # Calculate the average floor price.
    avg_floor_price = df[17].mean()
    print("Average Floor Price from sample:", avg_floor_price)
    
    # Save the model parameter (for example, a floor price threshold) to a JSON file.
    model_params = {"floor_price_threshold": avg_floor_price}
    with open("trained_model.json", "w") as f:
        json.dump(model_params, f)
    print("Model saved to trained_model.json")

if __name__ == "__main__":
    train_model()
