"""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# of solves: 1

Confidence: 5
"""

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        result = []

        ROW, COL = len(heights), len(heights[0])
        pac, atl = set(), set() 

        def dfs(i, j, heights, ocean, prev_height):
            if i < 0 or j < 0 or i == ROW or j == COL or (i, j) in ocean or prev_height > heights[i][j]:
                return
            
            ocean.add((i,j))
            curr_height = heights[i][j]
            dfs(i - 1, j, heights, ocean, curr_height)
            dfs(i + 1, j, heights, ocean, curr_height)
            dfs(i, j - 1, heights, ocean, curr_height)
            dfs(i, j + 1, heights, ocean, curr_height)

        # Top and bottom
        for j in range(COL):
            dfs(0, j, heights, pac, heights[0][j])
            dfs(ROW - 1, j, heights, atl, heights[ROW - 1][j])

        # Left and right
        for i in range(ROW):
            dfs(i, 0, heights, pac, heights[i][0])
            dfs(i, COL - 1, heights, atl, heights[i][COL - 1])

        # Go through matrix and find intersecting paths
        for i in range(ROW):
            for j in range(COL):
                if (i, j) in pac and (i, j) in atl:
                    result.append([i, j])

        return result

"""
Solution:
    1. For the top and bottom, which are Pacific and Atlantic respectively, run a DFS to add reachable paths to their own sets
    2. Do the same for left and right
    3. Run through the matrix and check for cells that are in both sets

Time complexity:
    1. Let m, n denote the size of heights
    2. O(mn)

Space complexity:
    1. Let m, n denote the size of heights
    2. O(mn)
"""