"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1] * len(nums)
        mult_backwards, mult_forwards = 1, 1
        for i in range(len(nums) - 2, -1, -1):
            mult_backwards *= nums[i + 1]
            result[i] = mult_backwards
        for i in range(1, len(nums)):
            mult_forwards *= nums[i - 1]
            result[i] *= mult_forwards
        return result
    
"""
Solution:
    1. Create an array of length nums
    2. Iterate backwards through nums, filling in the result array so that result[i] = all numbers multiplied to the right of i
    3. Iterate forwards through nums, multiplying the ith value in result with the product of numbers to the left of i in nums

Time complexity:
    1. Let n be the length of nums
    2. O(n)

Space complexity:
    1. Result array does not count as additional space in this problem
    2. O(1)
"""