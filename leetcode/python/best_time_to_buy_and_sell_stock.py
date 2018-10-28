"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


### Notes ###

* Read the f*ing question!@#!


l r dip delta  comments
7 1 T   -6     buy at 1
1 5 F    4     5-1 = 4
5 3 T   -2
3 6 F    3     6-1 = 5 **
6 4 T   -2

l r dip delta
7 6 T   -1
6 4 T   -2
4 3 T   -1
3 1 T   -2

[1, 2, 4]

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num_prices = len(prices)
        if num_prices in set([0, 1]):
            return 0
        elif num_prices == 2:
            if prices[1] >= prices[0]:
                return prices[1] - prices[0]

        li = 0
        ri = 1
        bottom = prices[0]
        max_profit = 0

        while ri < num_prices:
            l = prices[li]
            r = prices[ri]
            dip = l > r

            if dip:
                bottom = min(bottom, r)
            else:
                max_profit = max(max_profit, r - bottom)

            li += 1
            ri += 1

        return max_profit
