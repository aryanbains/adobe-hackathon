import pandas as pd
import os
from collections import defaultdict

def aggregate_all_data(dataset_dir="dataset", sample_only=True):
    """
    Aggregates auction, impression, click, and conversion data from log files.
    Returns a DataFrame with metrics calculated per AdvertiserID.
    
    Parameters:
    - dataset_dir (str): Path to the dataset directory.
    - sample_only (bool): If True, processes only the first chunk of each file.
    """
    stats = defaultdict(lambda: {
        'auction': 0,
        'impression': 0,
        'click': 0,
        'conversion': 0,
        'cost': 0.0
    })
    
    suffixes = [f"{i:02d}" for i in range(6, 13)]  # ['06', '07', ..., '12']
    
    def process_file(file_path, col_index, metric, cost_index=None):
        """Helper function to process log files."""
        if not os.path.exists(file_path):
            print(f"File not found: {file_path} (Skipping)")
            return
        
        print(f"Processing {file_path} for {metric} (sample)...")
        for chunk in pd.read_csv(
            file_path, sep=r"\s+", header=None, chunksize=100000, engine="python", on_bad_lines="skip"
        ):
            if col_index not in chunk.columns:
                print(f"Column {col_index} (AdvertiserID) not found in {file_path}. Skipping chunk.")
                break
            chunk[col_index] = pd.to_numeric(chunk[col_index], errors="coerce").dropna()
            groups = chunk.groupby(col_index).size()
            for adv_id, count in groups.items():
                stats[int(adv_id)][metric] += count
            
            if cost_index is not None:
                chunk[cost_index] = pd.to_numeric(chunk[cost_index], errors="coerce").dropna()
                cost_groups = chunk.groupby(col_index)[cost_index].sum()
                for adv_id, total_price in cost_groups.items():
                    stats[int(adv_id)]['cost'] += total_price / 1000.0  # Convert micro-currency to standard
            
            if sample_only:
                break
    
    # Process logs
    for sfx in suffixes:
        process_file(os.path.join(dataset_dir, f"bid.{sfx}.txt"), 22, "auction")
        process_file(os.path.join(dataset_dir, f"imp.{sfx}.txt"), 22, "impression", 20)
        process_file(os.path.join(dataset_dir, f"clk.{sfx}.txt"), 22, "click")
        process_file(os.path.join(dataset_dir, f"conv.{sfx}.txt"), 22, "conversion")
    
    # Build the final DataFrame
    rows = []
    for adv_id, agg in stats.items():
        auctions, imps, clicks, convs, cost = agg.values()
        
        rows.append({
            "AdvertiserID": adv_id,
            "Auction": auctions,
            "Impression": imps,
            "Click": clicks,
            "Conversion": convs,
            "Cost": cost,
            "Win-Rate": (imps / auctions) if auctions > 0 else 0,
            "CPM": (cost / imps * 1000) if imps > 0 else 0,
            "eCPC": (cost / clicks) if clicks > 0 else 0,
            "CTR": (clicks / imps) if imps > 0 else 0,
            "CVR": (convs / clicks) if clicks > 0 else 0
        })
    
    df_stats = pd.DataFrame(rows).sort_values(by="AdvertiserID")
    return df_stats

if __name__ == "__main__":
    df = aggregate_all_data(dataset_dir="dataset")
    print("\n----- Aggregated Stats by AdvertiserID -----")
    print(df.to_string(index=False))
    df.to_csv("aggregated_stats.csv", index=False)
