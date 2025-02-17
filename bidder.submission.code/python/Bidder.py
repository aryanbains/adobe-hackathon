# bidder.py
class Bidder:
    def getBidPrice(self, bidRequest):
        """
        Should be implemented by subclasses.
        Given a BidRequest instance, return the bid price (an integer) or -1 if not bidding.
        """
        raise NotImplementedError("Subclasses must implement this method.")
