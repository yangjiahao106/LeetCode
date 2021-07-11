from typing import *


class Solution:
    def largestArea(self, grid: List[str]) -> int:
        for i, row in enumerate(grid):
            grid[i] = list(row)

        def dfs(i, j) -> int:
            if grid[i][j] == 'x':
                return 0
            count = 1

            v = grid[i][j]
            grid[i][j] = 'x'  # 标记删除
            for dx, dy in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                x = i + dx
                y = j + dy
                if 0 <= x < len(grid) and 0 <= y < len(grid[0]):
                    if v == '0' or v == grid[x][y]:
                        count += dfs(x, y)
            return count

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '0':
                    dfs(i, j)
                if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                    dfs(i, j)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 'x':
                    c = dfs(i, j)
                    res = max(res, c)
        return res


if __name__ == '__main__':
    print(Solution().largestArea(["554350243", "325420343", "333515002", "054425245", "041533100", "345521331", "114302205", "555403522", "101315123", "111034215"]))
