"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

# of solves: 1
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left, right = 0, len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return [left + 1, right + 1]
    
"""
Solution:
    1. Initialize a pointer to the left and to the right
    2. Check the sum of the numbers at these pointers while they do not overlap
    3. If sum is less than our target, then shift left pointer
    4. If sum is greater than our target, then shift right pointer
    5. If sum is equal to our target, then return our left and right pointer added by one which denotes the one-based indexes of the two numbers that sum up to our target

Time complexity:
    1. Let n be the length of numbers
    2. O(n)

Space complexity:
    1. O(1)
"""