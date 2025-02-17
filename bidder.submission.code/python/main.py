# main.py
from bidrequest import BidRequest
from bid import Bid

def main():
    # Create a sample BidRequest with example data.
    sample_bid_request = BidRequest(
        bidId="sample_bid_001",
        timestamp="20250217123000000",
        visitorId="visitor_001",
        userAgent="Mozilla/5.0",
        ipAddress="192.168.1.1",
        region="1",
        city="1",
        adExchange="2",
        domain="sampledomain",
        url="http://sampleurl.com",
        anonymousURLID=None,
        adSlotID="12345",
        adSlotWidth="300",
        adSlotHeight="250",
        adSlotVisibility="FirstView",
        adSlotFormat="Fixed",
        adSlotFloorPrice="100",  # Example floor price
        creativeID="creative_001",
        advertiserId="1458",
        userTags="tag1,tag2"
    )
    
    bidder = Bid()
    bid_price = bidder.getBidPrice(sample_bid_request)
    print("Bid Price:", bid_price)

if __name__ == "__main__":
    main()
