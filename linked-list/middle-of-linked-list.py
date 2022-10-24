"""
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.
"""

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        slow, fast = head, head
        if not fast.next:
            return slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


"""
Solution:
    1. Create two pointers, one fast and one slow
    2. While fast pointer is not null and doesn't point to null, we move fast pointer twice and slow once
    3. Base case where fast pointer initially points to null, meaning that there's only one node in list

Time complexity:
    1. Let n be the number of nodes in the linked list
    2. O(n/2) = O(n)
"""