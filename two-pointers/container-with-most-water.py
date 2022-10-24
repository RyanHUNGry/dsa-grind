"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left_pointer, right_pointer = 0, len(height) - 1
        max_area = 0
        
        while (left_pointer < right_pointer):
            max_area = max(max_area, min(height[left_pointer], height[right_pointer]) * (right_pointer - left_pointer))
            if (height[left_pointer] < height[right_pointer]):
                left_pointer += 1
            else:
                right_pointer -= 1
        
        return max_area

"""
Solution:
    1. Set left and right pointers
    2. Calculate area and check for max
    3. Move the smaller pointer

Time complexity:
    1. Let n be the length of height
    1. O(n)
"""