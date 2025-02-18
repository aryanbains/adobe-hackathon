import pandas as pd
import os
import json

def train_model():
    """
    Reads imp.06.txt from the dataset folder, computes the average floor price (column 18),
    and saves it as 'floor_price_threshold' in trained_model.json.
    """
    file_path = os.path.join("dataset", "imp.06.txt")
    if not os.path.exists(file_path):
        print("File not found:", file_path)
        return

    chunk_size = 100000  # Process 100k rows at a time to handle large files
    total_sum = 0
    total_count = 0

    # Read the file in chunks
    for chunk in pd.read_csv(file_path, sep="\t", header=None, chunksize=chunk_size):
        # Column 17 (0-based) is adSlotFloorPrice
        # Convert to numeric, ignoring errors
        chunk[17] = pd.to_numeric(chunk[17], errors="coerce")
        # Drop rows where floor price is NaN
        chunk = chunk.dropna(subset=[17])

        total_sum += chunk[17].sum()
        total_count += chunk[17].count()

    if total_count == 0:
        avg_floor_price = 0
    else:
        avg_floor_price = total_sum / total_count

    # Save this average as our 'trained' threshold
    model_params = {"floor_price_threshold": avg_floor_price}

    with open("trained_model.json", "w") as f:
        json.dump(model_params, f, indent=2)

    print(f"Trained model saved to trained_model.json")
    print(f"Average Floor Price = {avg_floor_price:.2f}")

if __name__ == "__main__":
    train_model()
