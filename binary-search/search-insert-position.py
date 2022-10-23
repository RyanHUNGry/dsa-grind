"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)

    def binary_search(self, nums, target, low, high):
        if low > high:
            return low

        midpoint = (high + low)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            return self.binary_search(nums, target, midpoint + 1, high)
        else:
            return self.binary_search(nums, target, low, midpoint - 1)
        
"""
Solution:
    1. If the target exists in nums, this is just standard binary search
    2. We will modify our breaking case so that we return low, because that is where our missing element will go
"""