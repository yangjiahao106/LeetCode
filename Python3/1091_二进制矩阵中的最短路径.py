from typing import *


class Solution:
    """
    深度优先遍历可以求出最优解

    思路是按照距离一步一步往外扩张，通过visited 矩阵记录已经遍历过的点。 如果走到到已经遍历过的点，则之前到达的距离肯定比此次到达的距离更近（bfs），可以直接跳过。
    最终的结果就是最优解
    """

    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1: return -1

        # visited = [[0] * len(grid) for _ in range(len(grid[0]))] # 直接更新 grid 替代 visited
        dist = 0

        cur_level = {(0, 0)}
        grid[0][0] = 1
        while cur_level:
            dist += 1
            next_level = set()
            for pot in cur_level:
                i, j = pot[0], pot[1]
                # visited[i][j] = 1

                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return dist

                directions = [(i - 1, j - 1),
                              (i - 1, j),
                              (i - 1, j + 1),
                              (i, j + 1),
                              (i + 1, j + 1),
                              (i + 1, j),
                              (i + 1, j - 1),
                              (i, j - 1)]

                for d in directions:

                    if d[0] < 0 or d[1] < 0 or d[0] >= len(grid) or d[1] >= len(grid[0]):
                        continue
                    # if visited[d[0]][d[1]] == 1:
                    #     continue
                    if grid[d[0]][d[1]] == 1:
                        continue
                    grid[d[0]][d[1]] = 1  # 标记为已经遍历
                    next_level.add(d)

            cur_level = next_level

        return -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix([[0, 0, 0, 0, 1],
                                               [1, 0, 0, 0, 0],
                                               [0, 1, 0, 1, 0],
                                               [0, 0, 0, 1, 1],
                                               [0, 0, 0, 1, 0]]))
