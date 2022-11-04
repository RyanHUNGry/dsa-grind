"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# of solves: 2

# Confidence: 10
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        
        for num in nums:
            if num in hashset:
                return True
            else:
                hashset.add(num)
        return False

"""
Solution:
    1. For each number, put in set
    2. If number is already in set, return True

Time complexity:
    1. Let n be the length of nums:
    2. O(n)

Space complexity:
    1. O(n)
"""