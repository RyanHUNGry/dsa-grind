"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

# of solves: 1

Confidence: 3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        
        return self.createBranch(0, len(nums) - 1, nums)

    def createBranch(self, left, right, nums):
        if right < left:
            return None
        
        mid = (right + left)//2
        root = TreeNode(nums[mid])
        root.left = self.createBranch(left, mid - 1, nums)
        root.right = self.createBranch(mid + 1, right, nums)

        return root

"""
Solution:
    1. We know that the middle of the list will always be the root node, and we can use recursion to construct left and right nodes
    2. We will construct left branch first, and then right branch by calculating the midpoint
    3. When our right < left, we know to return null

Time complexity:
    1. Let n be the length of nums
    2. O(n) --> going through each number in nums once recursively

Space complexity
    1. Let n be the length of nums
    2. O(logn) --> tree is gauranteed to be balanced
"""