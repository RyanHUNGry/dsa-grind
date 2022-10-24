"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
"""

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """ 
        windowStart = 0
        max_sum, sum = float('-inf'), 0

        for num in nums:
            sum += num
            max_sum = max(max_sum, sum)
            while (sum < 0):
                sum -= nums[windowStart]
                windowStart += 1
        
        return max_sum
        
"""
Solution:
    1. Initialize two pointers to form a sliding window
    2. For each number in nums, add the number to a count by expanding window, then compare your count to a max
    3. If this count is < 0, shrink window until count is greater than 0 again

Time complexity:
    1. Let n be the length of nums
    2. O(n)

Space complexity:
    1. O(1)
"""