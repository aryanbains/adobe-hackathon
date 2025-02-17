// Bid.java
package com.dtu.hackathon.bidding;

import java.util.Random;

public class Bid implements Bidder {

    private int bidRatio = 50;         // 50% chance to bid
    private int fixedBidPrice = 300;   // Fixed bid price

    @Override
    public int getBidPrice(BidRequest bidRequest) {
        int bidPrice = -1;
        try {
            int floorPrice = Integer.parseInt(bidRequest.getAdSlotFloorPrice());
            // Do not bid if our fixed price is below the floor price.
            if (fixedBidPrice < floorPrice) {
                return -1;
            }
        } catch(Exception e) {
            // If an exception occurs, assume floor price is 0.
        }
        Random random = new Random();
        if(random.nextInt(100) < bidRatio) {
            bidPrice = fixedBidPrice;
        }
        return bidPrice;
    }
}
