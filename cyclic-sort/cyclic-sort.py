"""
We are given an array containing n objects. Each object, when created, was assigned a unique number from the range 1 to n based on their creation sequence. This means that the object with sequence number 3 was created just before the object with sequence number 4.

Write a function to sort the objects in-place on their creation sequence number in O(n) and without using any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.
"""

class Solution(object):
    def cyclicSort(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            # If the number at the current index is invalid, then we keep swapping
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            # Else, we move onto the next index
            else:
                i += 1
        return nums

"""
Solution:
    1. For each number in nums, keep swapping it into its index until the current index you're at is valid
    2. If valid, then move onto the next number

Time complexity:
    1. Let n be the length of nums
    2. O(n)

Space complexity:
    1. O(1)
"""