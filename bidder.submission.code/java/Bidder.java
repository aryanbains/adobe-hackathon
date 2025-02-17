// Bidder.java
package com.dtu.hackathon.bidding;

public interface Bidder {
    /**
     * Given a BidRequest, returns the bid price (an integer) or -1 if no bid is made.
     */
    int getBidPrice(BidRequest bidRequest);
}
