"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        window_start, count, min_length = 0, 0, float('inf')
        for i in range(len(nums)):
            count += nums[i]
            while (count >= target):
                min_length = min(min_length, i - window_start + 1)
                count -= nums[window_start]
                window_start += 1
        return min_length if min_length != float('inf') else 0
"""
Solution:
    1. Expand window and add numbers to a count
    2. If this count is larger or equal to target, compare the length of the window with the min
    3. Then, shrink window until count is no longer larger or equal to target
    
Time complexity:
    1. Let n be the length of nums
    2. O(n)

Space complexity:
    1. O(1)
"""