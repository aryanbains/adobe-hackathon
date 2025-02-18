#!/usr/bin/python
# -*- coding:utf8 -*-
import random


class Bid(object):

    def __init__(self):
        # Ratio of bidding in percent
        self.bid_ratio = 50
        # Fixed bid price
        self.fixed_bid_price = 300

    def get_bid_price(self, bidRequest):
        bid_price = -1
        if random.randint(0, 99) < self.bid_ratio:
            bid_price = self.fixed_bid_price
        return bid_price