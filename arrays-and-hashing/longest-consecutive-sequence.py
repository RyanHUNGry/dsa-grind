"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

# of solves: 2
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_length = 0
        hashset = set(nums)

        for num in nums:
            length, next_num = 1, num
            while num - 1 not in hashset and next_num + 1 in hashset:
                length += 1
                next_num += 1
            max_length = max(max_length, length)
        return max_length
        
"""
Solution:
    1. Put all numbers into a set
    2. For each number, check if it is the start of a sequence by checking for the existence of a right neighbor
    and the non-existence of a left neighbor
    3. If a number is the start of a sequence, count the length of the sequence and compare to max

Time complexity:
    1. Let n be the length of nums
    2. Let m be the average length of a sequence in nums
    3. O(n) + O(n * m) = O(n * m)

Space complexity:
    1. O(n)
"""
