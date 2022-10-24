"""
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            j = nums[i]
            if j > 0 and j <= len(nums) and j != i + 1 and j != nums[j - 1]:
                nums[i], nums[j - 1] = nums[j - 1], nums[i]
            else:
                i += 1
        for i, num in enumerate(nums):
            if num - 1 != i:
                return i + 1
        return len(nums) + 1
            
"""
Solution:
    1. For each index, we will swap numbers that are in range and are greater than 0 and aren't correct
    2. We will use 1-based indexing, which means 0 corresponds to 1 and so on; this is because 1 is the first positive integer, and having 0 as a correct value doesn't make sense; also check for infinite loops because you can have duplicate values
    3. We will go through the sorted array and return the index + 1 of the first incorrect index-value pair
    4. If all index-value pairs are correct, return length + 1

Time complexity
    1. Let n be the length of nums
    2. O(2n) = O(n)

Space complexity:
    1. O(1)
"""