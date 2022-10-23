"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.  
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        wordFound, count = False, 0
        for i in range(len(s) -1 , -1, -1):
            if s[i] == ' ' and wordFound: return count
            if s[i] != ' ':
                wordFound = True
                count += 1
        return count
        
"""
Solution:
    1. Initialize a boolean variable that marks whether or not you are on the last word
    2. Loop backwards, and set the boolean variable to true as soon as you see a non-space
    3. Count characters until you see a another space, which you can check with your boolean variable

Time complexity:
    1. Let n be the length of s
    2. O(n) --> no spaces at all
"""