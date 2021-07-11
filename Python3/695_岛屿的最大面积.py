from typing import *


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def legal(i, j) -> bool:
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                return False
            return True

        def helper(i, j) -> int:
            count = 1

            grid[i][j] = 0  # 将1标记为0 防止重复搜索

            dires = [(-1, 0), (0, -1), (1, 0), (0, 1)]  # 四个方向 方便计算

            for d in dires:
                if legal(i + d[0], j + d[1]) and grid[i + d[0]][j + d[1]] == 1:
                    count += helper(i + d[0], j + d[1])

            return count

        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    res = max(res, helper(i, j))

        return res


class Solution2:
    def dfs(self, grid, i, j) -> int:
        if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]) or grid[i][j] != 1:
            return 0
        grid[i][j] = 0
        ans = 1
        for di, dj in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
            next_i, next_j = i + di, j + dj
            ans += self.dfs(grid, next_i, next_j)
        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        for i, l in enumerate(grid):
            for j, n in enumerate(l):
                ans = max(self.dfs(grid, i, j), ans)
        return ans
