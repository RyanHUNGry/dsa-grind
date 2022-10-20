"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        res = []
        
        for num in nums:
            count[num] = count.get(num, 0) + 1
        for key, val in count.items():
            if not freq[val]:
                freq[val] = [key]
            else:
                freq[val] += [key]
        for i in range(len(freq) - 1, 0, -1):
            if freq[i]:
                k -= len(freq[i])
                res += freq[i]
            if (k == 0):
                return res

"""
Solution:
    1. Create dictionary of counts
    2. Create a list of lists that is the length of nums
    3. The index of the list represents the counts, and the values represent all numbers that have that count
    4. From count dictionary, move everything to list
    5. Iterate backwards from list and obtain the k-most frequent elements
    
Time complexity:
    1. n is the length of nums
    2. O(n) + O(n) + O(n) + O(n) = O(n)
"""
        