# bidrequest.py
class BidRequest:
    def __init__(self,
                 bidId=None,
                 timestamp=None,
                 visitorId=None,
                 userAgent=None,
                 ipAddress=None,
                 region=None,
                 city=None,
                 adExchange=None,
                 domain=None,
                 url=None,
                 anonymousURLID=None,
                 adSlotID=None,
                 adSlotWidth=None,
                 adSlotHeight=None,
                 adSlotVisibility=None,
                 adSlotFormat=None,
                 adSlotFloorPrice=None,
                 creativeID=None,
                 advertiserId=None,
                 userTags=None):
        self.bidId = bidId
        self.timestamp = timestamp
        self.visitorId = visitorId
        self.userAgent = userAgent
        self.ipAddress = ipAddress
        self.region = region
        self.city = city
        self.adExchange = adExchange
        self.domain = domain
        self.url = url
        self.anonymousURLID = anonymousURLID
        self.adSlotID = adSlotID
        self.adSlotWidth = adSlotWidth
        self.adSlotHeight = adSlotHeight
        self.adSlotVisibility = adSlotVisibility
        self.adSlotFormat = adSlotFormat
        self.adSlotFloorPrice = adSlotFloorPrice
        self.creativeID = creativeID
        self.advertiserId = advertiserId
        self.userTags = userTags

    def __str__(self):
        return f"BidRequest(bidId={self.bidId}, adSlotFloorPrice={self.adSlotFloorPrice})"
