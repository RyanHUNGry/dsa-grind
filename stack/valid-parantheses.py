"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        conversions = {'}': '{', ']': '[', ')': '('}

        for char in s:
            converted = conversions.get(char)
            if not converted:
                stack.append(char)
            if converted:
                if len(stack) == 0 or stack[-1] != converted:
                    return False
                stack.pop()
        
        return len(stack) == 0
            

"""
Solution:
    1. Loop through every character in s
    2. If you see an open character, add it to the stack
    3. If you see a closed character, check its correct pair and see if its on top of the stack
    4. If stack is empty or incorrect open character, then return false
    5. Edge case where you only have opening brackets, and so you return !stack.empty()

Time complexity:
    1. Let n be the length of s
    2. O(n)

Space complexity:
    1. O(n)
"""