import sys
from bidrequest import BidRequest
from bid import Bid

def run_bidding():
    # Create a sample BidRequest
    sample_bid_request = BidRequest(
        bidId="sample001",
        adSlotFloorPrice="120"
    )
    bidder = Bid()
    price = bidder.getBidPrice(sample_bid_request)
    print("Bid Price:", price)

def run_aggregated_stats():
    # Import the aggregator function and run it
    from aggregate_stats import aggregate_all_data
    df = aggregate_all_data(dataset_dir="../dataset")
    print("\n----- Aggregated Stats by AdvertiserID -----")
    print(df.to_string(index=False))

if __name__ == "__main__":
    if "--agg" in sys.argv:
        run_aggregated_stats()
    else:
        run_bidding()
