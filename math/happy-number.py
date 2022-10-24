"""
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.
"""

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow, fast = n, n
        while fast != 1:
            slow = self.computeHappy(slow)
            fast = self.computeHappy(self.computeHappy(fast))
            if (fast == 1):
                return True
            if (slow == fast):
                return False
        
        return True

    def computeHappy(self, n):
        sum = 0
        while n != 0:
            sum += (n % 10)**2
            n //= 10
        return sum

"""
Solution:
    1. We will write a function that will compute the next number given the formula
    2. We will have a slow pointer and a fast pointer
    3. The fast pointer will be the result of using our formula function twice; slow is just once
    4. We will keep looping until our fast pointer equals 1
    5. Inside our loop, we will have a breaking condition that is slow = fast because this denotes a cycle
    6. Before this breaking condition, however, we have to check if fast is equal to 1 first because there may be a case where fast == slow and fast == 1

Time complexity:
    1. Let k be the number of steps to go from n to 1
    2. O(logk)
"""