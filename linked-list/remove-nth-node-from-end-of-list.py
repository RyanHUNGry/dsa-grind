"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast, slow = head, head
        
        for i in range(n):
            fast = fast.next
        
        if (fast == None):
            return slow.next
        
        while (fast.next != None):
            fast = fast.next
            slow = slow.next
        
        slow.next = slow.next.next
        
        return head
        
"""
Solution:
    1. Fast and slow pointers; give fast pointer an n-step head start
    2. Move pointers until fast pointer's next element is null
    3. Your slow pointer will be at the node before the one to remove
    4. Deal with edge case of removing first node in list, which happens when your fast pointer is siting on null; basically remove the next pointer of the slow pointer

Time complexity:
    1. n is the length of n
    2. O(n)
"""