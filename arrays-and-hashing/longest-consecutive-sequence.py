"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Create set of numbers
        hashset = set(nums) 
        longest_consecutive = 1

        # For each number in the list
        for num in nums:
            curr = num
            consecutive = 1
            # Check if that number is the start of a sequence by checking if there isn't a left neighbor and if there is a right neighbor 
            while num - 1 not in hashset and curr + 1 in hashset:
                consecutive += 1
                curr += 1
            longest_consecutive = max(longest_consecutive, consecutive)
        
        return longest_consecutive if nums else 0

"""
Solution:
    1. Put all numbers into a set
    2. For each number in nums, check to see if it is the start of a sequence by seeing if its left neighbor doesn't exist in the set
    3. If the number is the start of a sequence, do a while loop to check how long that sequence is
    4. If the number isn't the start of a sequence, don't do anything
 
Time complexity:
    1. Let n be the length of nums
    2. O(n)

Space complexity:
    1. O(n)
"""