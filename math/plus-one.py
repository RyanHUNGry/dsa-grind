"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1

        while (digits[i] + 1 == 10 and i >= 0):
            digits[i] = 0
            i -= 1
        else:
            if (i < 0): 
                digits = [1] + digits
                return digits
            digits[i] += 1
        return digits
        
"""
Solution:
    1. We will do a while loop going backwards
    2. While digits[i] + 1 is equal to 10 and i is in bounds, set digit at i to 0, and then decrement i
    3. Else, simply add the 1 to the current digit at i, or if i is out of bounds, then concantenate [1] to the front of digits
    4. 

Time complexity:
    1. Let n be the number of digits in digits
    2. O(n) --> when all digits are 9
"""