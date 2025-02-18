import os
import json
import pickle
from datetime import datetime
from bidrequest import BidRequest
from bidder import Bidder

class Bid(Bidder):
    def __init__(self):
        # Load pre-trained models and config
        self.models = self._load_models()
        self.advertiser_config = {
            1458: {'N': 0, 'budget': 350000},
            3358: {'N': 2, 'budget': 300928},
            3386: {'N': 0, 'budget': 350000},
            3427: {'N': 0, 'budget': 350000},
            3476: {'N': 10, 'budget': 350000}
        }
        self.spent = {campaign: 0 for campaign in self.advertiser_config}
        
    def _load_models(self):
        """Load pre-trained ML models"""
        model_path = os.path.join(os.path.dirname(__file__), "models.pkl")
        try:
            with open(model_path, "rb") as f:
                return pickle.load(f)  # Contains ctr_model, cvr_model, price_model
        except Exception as e:
            raise RuntimeError(f"Model loading failed: {str(e)}")

    def _extract_features(self, bid_request):
        """Feature engineering pipeline"""
        # Temporal features
        hour = int(bid_request.timestamp[8:10]) if bid_request.timestamp else 0
        
        # Device features
        is_mobile = "Mobile" in bid_request.userAgent if bid_request.userAgent else False
        
        return [
            hour,
            is_mobile,
            bid_request.adSlotWidth,
            bid_request.adSlotHeight,
            int(bid_request.adSlotFloorPrice) if bid_request.adSlotFloorPrice else 0,
            self.advertiser_config[bid_request.advertiserId]['N']
        ]

    def getBidPrice(self, bid_request: BidRequest) -> int:
        """Real-time bidding decision engine"""
        # 1. Get advertiser config
        config = self.advertiser_config.get(bid_request.advertiserId)
        if not config or self.spent[bid_request.advertiserId] >= config['budget']:
            return -1

        # 2. Feature extraction
        features = self._extract_features(bid_request)
        
        # 3. Model predictions
        ctr = self.models['ctr_model'].predict_proba([features])[0][1]
        cvr = self.models['cvr_model'].predict_proba([features])[0][1]
        market_price = self.models['price_model'].predict([features])[0]
        
        # 4. Value calculation
        expected_value = ctr + (config['N'] * cvr)
        bid_price = min(expected_value * 1000, config['budget'] - self.spent[bid_request.advertiserId])
        
        # 5. Budget-aware bidding
        if bid_price > market_price and bid_price > bid_request.adSlotFloorPrice:
            self.spent[bid_request.advertiserId] += market_price  # 2nd price auction
            return int(bid_price)
        
        return -1