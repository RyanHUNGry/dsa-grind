"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] >= len(nums) or nums[i] == i:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
        
        for i, num in enumerate(nums):
            if i != num:
                return i
        return len(nums)
"""
Solution:
    1. For each index position, keep swapping numbers until you either have a number that is out of bounds or correct
    2. Run one more for loop to check each value-index pair and return the index of the mismatch
    3. If there is no mismatch, then we know that the value is at the length of the list

Time complexity:
    1. Let n be the length of nums
    2. O(2n) = O(n)

Space complexity: 
    1. O(1)
"""