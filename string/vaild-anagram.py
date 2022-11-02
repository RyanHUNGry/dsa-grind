"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

# of solves: 1

Confidence: 8
"""
from collections import Counter

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        counts = Counter(s) # Succinct way to get counts of an iterable
        
        for character in t:
             # Don't need to use get method to check non-existence because the Counter object returns 0 for missing values
            if counts[character] == 0:
                return False
            else:
                counts[character] -= 1

        return True
        
"""
Solution:
    1. Add all letters of s into a count hash table
    2. For each letter in t, check if the letter's count is 0 in the count hash table
    3. If it is 0, then we know that s has ran out of characters for t to use to assemble the anagram
    4. Otherwise, subtract 1 from the count of that letter
    5. Check edge case where s and t aren't equal in length

Time complexity:
    1. Let n be the length of s and m be the length of t
    2. O(n + m)

Space complexity:
    1. O(n)
"""