"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        previous, next, current = None, None, head

        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        return previous


"""
Solution:
     1. Initialize a previous pointer at null; a current pointer at head; a next pointer at null
     2. Iterate until current is null
     3. Set next as curr.next to store the next node
     4. Put curr.next to previous
     5. Set previous to curr
     6. set curr to next
     7. Return previous, which will be set at the first node
     
Time complexity:
    1. Let n be the number of nodes
    2. O(n)
"""