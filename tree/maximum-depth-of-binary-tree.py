"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# of solves: 1

Confidence: 5
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, depth):
            if not root:
                return depth
            return max(dfs(root.left, depth + 1), dfs(root.right, depth + 1))
        
        return dfs(root, 0)
"""
Solution:
    1. Run a DFS function that takes in a depth argument
    2. This depth argument will keep track of how deep we are in the tree at each level
    3. The function will traverse the tree to the very left, then to the very right and return the depth of the ends of the branches
    4. We will then compare which branch has the larger depth and return it

Time complexity:
    1. Let n be the number of nodes in the tree
    2. O(n)

Space complexity:
    1. Let h be the height of the tree
    2. O(h)
"""