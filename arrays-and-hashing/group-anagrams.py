"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hashmap = {}
        
        for str in strs:
            counts = [0 for i in range(26)]
            # Incrementing counts based on ASCII value of character
            for char in str:
                counts[ord(char) - 97] += 1
            hashmap[tuple(counts)] = hashmap.get(tuple(counts), []) + [str]

        return hashmap.values()

"""
Solution:
    1. For each string, create a 26-length list that will store counts of letters a-z (index of list is ASCII val - 65)
    2. Once we have the list, turn it into a tuple and set it as a key in the hashmap if it doesn't exist, as well as the value
    3. If the list does exist as a key, simply add the value to the existing value
    
Time complexity:
    1. n is the length of strs
    2. m is the average length of a str in strs
    2. O(n(m + 26)) = O(nm)

Space complexity:
    1. O(26n) = O(n)
"""