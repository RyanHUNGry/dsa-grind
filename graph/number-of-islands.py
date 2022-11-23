"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# of solves: 1

Confidence: 8
"""

# DFS solution:
# class Solution(object):
#     def numIslands(self, grid):
#         """
#         :type grid: List[List[str]]
#         :rtype: int
#         """
        
#         def dfs(i, j, grid):
#             if (i < 0 or i >= len(grid)) or (j < 0 or j >= len(grid[i])) or grid[i][j] == '0':
#                 return
            
#             grid[i][j] = '0'

#             dfs(i + 1, j, grid)
#             dfs(i - 1, j, grid)
#             dfs(i, j + 1, grid)
#             dfs(i, j - 1, grid)

#         num_islands = 0
#         for i in range(len(grid)):
#             for j in range(len(grid[i])):
#                 if grid[i][j] == '1':
#                     num_islands += 1
#                     dfs(i, j, grid)
            
#         return num_islands

# BFS solution:
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(i, j, grid):
            # create queue and add root node to queue
            queue = []
            queue.append((i, j))
            # mark root as visited
            grid[i][j] = 0

            while queue:
                # pop node from queue
                i, j = queue.pop()
                # check if node is valid
                if not (i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0'):
                     grid[i][j] = '0'
                     queue.append((i + 1, j))
                     queue.append((i - 1, j))
                     queue.append((i, j + 1))
                     queue.append((i, j - 1))

        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    num_islands += 1
                    bfs(i, j, grid)
        
        return num_islands
"""
Solution:
    1. Loop through each cell
    2. If the cell is a 1, add to counter and then run a DFS to traverse the entire island to mark it off as 0
    3. We can use BFS in this case as well

Time complexity:
    1. Let m, n denote the size of the grid
    2. O(mn)

Space complexity:
    1. Let m, n denote the size of the grid
    2. O(mn)
"""