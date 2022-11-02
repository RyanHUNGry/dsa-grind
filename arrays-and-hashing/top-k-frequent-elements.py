"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# of solves: 2
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        count = [[] for i in range(len(nums))] # Do not use [[]] * len(nums) because this copies the reference across the inner arrays
        count_dict = {}

        for num in nums:
            count_dict[num] = count_dict.get(num, 0) + 1

        for num in count_dict:
            count[count_dict[num] - 1].append(num)

        for i in range(len(count) - 1, -1, -1):
            if count[i]:
                k -= len(count[i])
                result += count[i]
            if k == 0:
                return result

        return result
        
"""
Solution:
    1. Create an array that is the size of nums
    2. The index + 1 of this array will represent the number of occurences, and it will hold a list of values
    that occur said times
    3. For each value in nums, we can count the number of times it occurs using a dictionary and put it in the correct index position of the array
    4. Then, iterate backwards and append the k first numbers that you see into your result

Time complexity:
    1. O(n) + O(n) + O(n) = O(n)

Space complexity:
    1. O(n) + O(n) = O(n)
"""