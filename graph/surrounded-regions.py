"""
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

# of solves: 1

Confidence: 7
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        # BFS solution
        def bfs(i, j, board, new_val, original_val):
            queue = []
            queue.append((i, j))

            while queue:
                i, j = queue.pop()
                if not (i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != original_val):
                    board[i][j] = new_val
                    queue.append((i + 1, j))
                    queue.append((i - 1, j))
                    queue.append((i, j + 1))
                    queue.append((i, j - 1))


        # DFS solution 
        def dfs(i, j, board, new_val, original_val):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != original_val:
                return
            
            board[i][j] = new_val
            dfs(i + 1, j, board, new_val, original_val)
            dfs(i - 1, j, board, new_val, original_val)
            dfs(i, j + 1, board, new_val, original_val)
            dfs(i, j - 1, board, new_val, original_val)

        # Finding and converting boundary regions to T
        for i in range(len(board)):
            for j in range(len(board[0])):
                if i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1:
                    # These are border cells
                    bfs(i, j, board, "T", "O") # Can change to DFS()

        # Flipping all non-border regions to X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

        # Flipping boundary regions from T back to O
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

"""
Solution:
    1. Think of this problem as finding all regions connected to the border
    2. You can then flip any cell that is not a region
    3. Loop through border to find regions connected to it and run a BFS/DFS to convert these cell's to a temporary marker T
    4. Then, loop through the matrix and convert any cell that is O to X
    5. Then, loop through again and for every cell that is a T, convert it to O

Time complexity:
    1. Let m, n denote the size of board
    2. O(mn) + O(mn) + O(mn) = O(mn)

Space complexity:
    1. Let m, n denote the size of board
    2. O(mn)
"""