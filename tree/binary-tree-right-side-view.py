"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

# of solves: 1

Confidence: 8
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res, queue = [], [root]

        while queue:
            first = True
            for i in range(len(queue)):
                node = queue.pop(0)
                if first:
                    res.append(node.val)
                    first = False
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)

        return res
        
"""
Solution:
    1. Starting from root node, conduct a BFS going from right to left
    2. At each level, add the first node we pop from the queue to the result because this is the right-most node at the current level

Time complexity:
    1. Let n be the number of nodes in the tree
    2. O(n)

Space complexity:
    1. Let n be the number of nodes in the tree
    2. O(n) --> at the lowest level, we can have a maximum of n/2 nodes
"""