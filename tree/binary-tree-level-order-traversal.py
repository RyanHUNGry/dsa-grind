"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

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
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        res, queue = [],[]
        queue.append(root)
        
        while queue:
            nodes_in_level = []
            for i in range(len(queue)):
                node = queue.pop(0)
                nodes_in_level.append(node.val)
                # add the nodes left and right children
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(nodes_in_level)
        
        return res

"""
Solution:
    1. Starting from root node, conduct a BFS
    2. At each iteration of BFS, we know how many nodes are in our level given the queue length
    3. Remove every node at the level in the queue and add them to a result list while adding left and right children if they exist

Time complexity:
    1. Let n be the number of nodes in the tree
    2. O(n)

Space complexity:
    1. Let n be the number of nodes in the tree
    2. O(n) --> at the lowest level, we can have a maximum of n/2 nodes
"""