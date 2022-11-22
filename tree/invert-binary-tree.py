"""
Given the root of a binary tree, invert the tree, and return its root.

# of solves: 1

Confidence: 7
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    
        def dfs(root):
            if not root:
                return None
            left_branch = dfs(root.left)
            right_branch = dfs(root.right)
            root.left, root.right = right_branch, left_branch
            return root
            
        return dfs(root)    
    
"""
Solution:
    1. Using recursion, traverse left subtree first make sure left subtree is reversed
    2. Then, traverse right subtree to make sure right subtree is reversed
    3. Then, from your root node, assign to your left the right subtree and vice versa
    4. It does not matter whether we use pre-order or post-order (in this case, using )

Time complexity:
    1. Let n be the number of nodes in the tree
    2. O(n) --> we need to traverse through each node recursively

Space complexity: 
    1. Let n be the number of nodes in the tree
    2. O(n) --> happens when we are reversing an imbalanced tree, else o(h)
"""