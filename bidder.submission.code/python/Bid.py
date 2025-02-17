# bid.py
import random
import json
import os
from bidrequest import BidRequest
from bidder import Bidder

class Bid(Bidder):
    def __init__(self):
        # Baseline parameters; feel free to tune these.
        self.bidRatio = 50           # 50% chance to bid
        self.fixedBidPrice = 300     # Fixed bid price (in local currency per CPM)
        # Load the trained model parameter from JSON.
        self.floor_price_threshold = 0
        model_file = os.path.join("..", "..", "trained_model.json")
        # Adjust path if running from bidder.submission.code/python folder.
        if not os.path.exists("trained_model.json"):
            model_file = "trained_model.json"
        if os.path.exists(model_file):
            try:
                with open(model_file, "r") as f:
                    model_params = json.load(f)
                    self.floor_price_threshold = model_params.get("floor_price_threshold", 0)
            except Exception as e:
                print("Error loading model:", e)
        else:
            print("Model file not found, using default threshold 0")

    def getBidPrice(self, bidRequest: BidRequest) -> int:
        """
        Bidding strategy:
        1. Convert the ad slot floor price to an integer (default to 0 if missing).
        2. If the bid request's floor price exceeds our trained threshold, do not bid.
        3. Also, if our fixed bid price is below the ad slot's floor price, skip bidding.
        4. Otherwise, bid with a probability defined by bidRatio.
        """
        bidPrice = -1
        try:
            floor_price = int(bidRequest.adSlotFloorPrice) if bidRequest.adSlotFloorPrice is not None else 0
        except Exception:
            floor_price = 0

        # Use the trained threshold: skip if the floor price is above our threshold.
        if floor_price > self.floor_price_threshold:
            return -1

        # Also, do not bid if our fixed bid price is less than the floor price.
        if self.fixedBidPrice < floor_price:
            return -1

        # Random decision: bid with probability = bidRatio%
        if random.randint(0, 99) < self.bidRatio:
            bidPrice = self.fixedBidPrice

        return bidPrice
