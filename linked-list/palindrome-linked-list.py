"""
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
"""

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head

        # Edge case
        if not fast.next:
            return True

        # Get to middle of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, next = None, None

        # Reverse second half
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # Go through each half and compare values
        while prev:
            if prev.val != head.val: 
                return False
            prev = prev.next
            head = head.next
        
        return True

"""
Solution:
    1. Combine fast-and-slow pointers and linked list reversal
    2. Get to center of the list
    3. Reverse the second half of the list
    4. Go through each node of each half and then compare
    5. Deal with edge case of only one node

Time complexity:
    1. O(n)
"""