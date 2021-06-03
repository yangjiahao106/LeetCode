from typing import *


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        """
        从四周向内进行深度优先遍历， 将所有与边界相连的'O' 修改为 'A' ，剩下的'O' 就是被包围的'O' 
        之后将'O' 填充为'X' 将 'A' 再修改回'O'
        """

        for i in range(0, len(board)):
            self.dfs(board, i, 0)
            self.dfs(board, i, len(board[0]) - 1)

        for j in range(0, len(board[0])):
            self.dfs(board, 0, j)
            self.dfs(board, len(board) - 1, j)

        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'A':
                    board[i][j] = 'O'

    def dfs(self, board, i, j):
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
            return

        if board[i][j] != 'O':
            return

        board[i][j] = 'A'
        self.dfs(board, i - 1, j)
        self.dfs(board, i + 1, j)
        self.dfs(board, i, j - 1)
        self.dfs(board, i, j + 1)
