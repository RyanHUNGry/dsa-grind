"""
You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

The area of an island is the number of cells with a value 1 in the island.

Return the maximum area of an island in grid. If there is no island, return 0.
"""

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def bfs(i, j, grid):
            area = 0
            queue = []
            queue.append((i, j))

            while queue:
                i, j = queue.pop()
                if not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == 0):
                    grid[i][j] = 0
                    area += 1
                    queue.append((i + 1, j))
                    queue.append((i -1 , j))
                    queue.append((i, j + 1))
                    queue.append((i, j - 1))

            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    max_area = max(max_area, bfs(i, j, grid))
        
        return max_area


"""
Solution:
    1. For each cell, check if it is a 1
    2. If so, run BFS (or DFS) and have a counter to keep track of the area
    3. Compare the area to the max

Time complexity:
    1. Let m, n denote the size of the grid
    2. O(mn)

Space complexity:
    1. Let m, n denote the size of the grid
    2. O(mn)
"""