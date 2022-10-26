"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if (slow == fast):
                return True
        return False

"""
Solution:
    1. Initialize a slow and fast pointer
    2. Keep moving fast pointer until it is null or its next is null
    3. If slow pointer equals fast pointer, return true
    4. Return false as the base condition

Time complexity:
    1. Let n be the number of nodes
    2. O(n)

Space complexity:
    1. O(1)
"""