"""
Given a string s, find the length of the longest substring without repeating characters.

# of solves: 1

Confidence: 8
"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        window_start, max_length, hashset = 0, 0, set()

        for i, character in enumerate(s):
            while character in hashset:
                hashset.remove(s[window_start])
                window_start += 1
            hashset.add(character)
            max_length = max(max_length, i - window_start + 1)

        return max_length

"""
Solution:   
    1. Check to see if the character you are on is in the set
    2. If the character is in the set, shrink window until character not in set
    3. If the character is not in the set, add it to the set
    4. Compute the length of the window

Time complexity:
    1. Let n be the length of s
    2. O(n)

Space complexity:
    1. O(1)
"""