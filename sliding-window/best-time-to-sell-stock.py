"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        
        left, right = 0, 1

        while right < len(prices):
            diff = prices[left] - prices[right]
            if (diff > 0):
                left = right
            else:
                max_profit = max(max_profit, abs(diff))
            right += 1

        return max_profit
        
        
"""
Solution:
    1. If prices length is 1, return 0
    2. Set a left pointer at index 0 and right pointer at index 1
    3. If difference between left pointer and right pointer is positive, then we set the left pointer to the right pointer
    4. Else if difference betwen pointers is positive, then we compare the profit to a max
    4. Increment right pointer until we are at the last stock in the list

Time complexity:
    1. n is the length of prices
    2. O(n)
"""