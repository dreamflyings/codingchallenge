"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

Say you have an array for which the ith element is the price of a given stock
on day i.

Design an algorithm to find the maximum profit. You may complete as many
transactions as you like (i.e., buy one and sell one share of the stock
multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you
must sell the stock before you buy again).

^^^ I suspect this is a broken assumption

"""


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        num_prices = len(prices)
        max_profit = 0

        profit = 0
        for j in range(1, num_prices):
            i = j - 1
            pi = prices[i]
            pj = prices[j]
            dip = pi < pj

            if not dip:
                profit += pi
            else:
                # sell when there is a dip, not sure whether this would cover all cases
                max_profit += profit
                profit = 0

            return max_profit
