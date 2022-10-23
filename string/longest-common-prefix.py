"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
"""

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""

        for i in range(len(strs[0])):
            for str in strs:
                if i == len(str) or str[i] != strs[0][i]:
                    return result
            result += strs[0][i]
        return result
"""
Solution:
    1. Use the first string in the list as your base comparator
    2. For each string, check to see if index is in bounds first; then check to see if the character of the comparator matches with the string
    3. If it doesn't, return
    4. After the check, add the character to result since we have checked that it exists in each string

Time complexity:
    1. Let n be the length of strs
    2. Let m be the shortest string in the list
    3. O(mn) --> basically the total number of characters of every string
"""