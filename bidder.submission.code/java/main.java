// Main.java
package com.dtu.hackathon.bidding;

public class Main {
    public static void main(String[] args) {
        BidRequest bidRequest = new BidRequest();
        bidRequest.setBidId("sample_bid_001");
        bidRequest.setTimestamp("20250217123000000");
        bidRequest.setVisitorId("visitor_001");
        bidRequest.setUserAgent("Mozilla/5.0");
        bidRequest.setIpAddress("192.168.1.1");
        bidRequest.setRegion("1");
        bidRequest.setCity("1");
        bidRequest.setAdExchange("2");
        bidRequest.setDomain("sampledomain");
        bidRequest.setUrl("http://sampleurl.com");
        bidRequest.setAnonymousURLID(null);
        bidRequest.setAdSlotID("12345");
        bidRequest.setAdSlotWidth("300");
        bidRequest.setAdSlotHeight("250");
        bidRequest.setAdSlotVisibility("FirstView");
        bidRequest.setAdSlotFormat("Fixed");
        bidRequest.setAdSlotFloorPrice("100"); // Example floor price
        bidRequest.setCreativeID("creative_001");
        bidRequest.setAdvertiserId("1458");
        bidRequest.setUserTags("tag1,tag2");
        
        Bid bidder = new Bid();
        int bidPrice = bidder.getBidPrice(bidRequest);
        System.out.println("Bid Price: " + bidPrice);
    }
}
