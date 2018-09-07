"""
### Problem ###

Take an array denoting the daily stock price and return the maximum
profit that could be made by buying and selling one share of that
stock.

### Notes ###

Brute force algorithm is simple, but is it possible to do better?

[310, 315, 275, 295, 260, 270, 290, 230, 255, 250]

i  price lowest profit
-        320    0
0  310   310    0
1  315   310    5
1  275   275    5
2  295   275    20
3  260   260    20
4  270   260    20
5  290   260    30 <--
6  230
7  255
8  250

"""

import unittest


class BuySellStockOnce(unittest.TestCase):
    def max_profit(self, prices):
        min_price = prices[0]
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price

            profit_if_sold = price - min_price

            if profit_if_sold > profit:
                profit = profit_if_sold

        return profit

    def test_basic(self):
        prices = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
        expected = 30
        actual = self.max_profit(prices)

        self.assertEqual(expected, actual)
