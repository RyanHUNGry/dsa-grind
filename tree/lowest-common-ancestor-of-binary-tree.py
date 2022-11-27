"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

# of solves: 1

Confidence: 7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        while root:
            if root.val == p.val or root.val == q.val or root.val > p.val and root.val < q.val or root.val > q.val and root.val < p.val:
                return root
            
            if root.val > p.val and root.val > q.val:
                root = root.left

            if root.val < p.val and root.val < q.val:
                root = root.right
        
"""
Solution:
    1. If the node you are on is less than both p and q, then move your node to the right child
    2. If the node you are on is bigger than both p and q, then move your node to the left child
    3. If the node you are on is equal to p, then return p and same for q
    4. If the node you are on is between the values of p and q, then return the node
    5. Use iteration here rather than recursion to save space

Time complexity:
    1. Let n be the number of nodes in the tree
    2. O(n)

Space complexity:
    1. O(1)
"""