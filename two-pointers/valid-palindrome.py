"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].lower().isalnum():
                left += 1
            while right > left and not s[right].lower().isalnum():
                right -= 1
            if (s[left].lower() != s[right].lower()): 
                return False
            left += 1
            right -= 1
        return True
"""
Solution:
    1. Set left and right pointers
    2. Keep moving left pointer if it isn't alphanumeric; then do the same for right
    2. Check LETTERS at the pointers
    3. If letters are not equal, return false
    4. After checking letters, move both pointers inwards
"""