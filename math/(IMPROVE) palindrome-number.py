"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0): return False
    
        temp_x = x
        divisor = 1
        while (temp_x//10 != 0):
            divisor *= 10
            temp_x //= 10
        
        while (divisor != 0):
            left_digit, right_digit = x//divisor, x % 10
            print(left_digit, right_digit)
            if left_digit != right_digit:
                return False
            x = (x % divisor)//10
            divisor //= 100
        
        return True
        
"""
Solution:
    1. Reverse x and compare it to itself
    2. Deal with edge case of x begin negative
    3. To reverse x, 

Time complexity:
    1. Let n be the number of digits of x
    2. O(n) + O(n/2) = O(n)
"""