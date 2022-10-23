"""
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binary_search(nums, target, 0, len(nums) - 1)
        
    def binary_search(self, nums, target, low, high):
        if low > high:
            return -1

        midpoint = (high + low)//2

        if nums[midpoint] == target:
            return midpoint
        elif nums[midpoint] < target:
            return self.binary_search(nums, target, midpoint + 1, high)
        else:
            return self.binary_search(nums, target, low, midpoint - 1)
        
"""
Solution:
    1. Create a recursive function that takes in nums, target, low, and high
    2. Call the recursive function with nums, target, 0, and len(nums) - 1
    3. Keep doing this until your low pointer is greater than high pointer, which is your breaking condition

Time complexity:
    1. Let n be the length of nums
    2. O(logn)
"""