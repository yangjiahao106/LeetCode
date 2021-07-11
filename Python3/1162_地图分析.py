from typing import *


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        from collections import deque
        row = len(grid)
        col = len(grid[0])

        dp = [[0] * col for _ in range(row)]

        def bfs(i, j) -> int:
            visited = [[0] * col for _ in range(row)]
            cur_queue = deque()
            next_queue = deque()
            cur_queue.append((i, j))
            count = 1
            while cur_queue:
                cur_i, cur_j = cur_queue.popleft()
                for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    cur_i, cur_j = cur_i + di, cur_j + dj
                    if cur_i < 0 or cur_j < 0 or cur_i >= row or cur_j >= col:
                        continue
                    if visited[cur_j][cur_j]:
                        continue

                    if grid[cur_i][cur_j] == 1:
                        dp[cur_i][cur_j] = count
                        return count

                    visited[cur_i][cur_j] = 1
                    next_queue.append((i + di, j + dj))

                if len(cur_queue) == 0:
                    count += 1
                    cur_queue, next_queue = next_queue, deque()

            return count

        res = -1
        hasOne = False  # 如果全部为0 则返回-1
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 0:
                    res = max(res, bfs(i, j))
                else:
                    hasOne = True
        if hasOne:
            return res
        else:
            return -1


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])

        cur_queue = list()
        next_queue = list()

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    cur_queue.append((i, j))

        count = 0
        while len(cur_queue) > 0:
            i, j = cur_queue.pop()
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ci, cj = i + di, j + dj

                if 0 <= ci < row and 0 <= cj < col and grid[ci][cj]:
                    next_queue.append((ci, cj))
                    grid[ci][cj] = 1

            if len(cur_queue) == 0 and len(next_queue) > 0:
                cur_queue = next_queue
                next_queue = list()
                count += 1

        return count if count else -1


import collections


class Solution3:

    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = collections.deque([(i, j) for i in range(n) for j in range(n) if grid[i][j]])
        if len(queue) == 0 or len(queue) == n * n:
            return -1

        distance = -1
        while queue:
            distance += 1
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < n and not grid[nx][ny]:
                        grid[nx][ny] = 1
                        queue.append((nx, ny))
        return distance


if __name__ == '__main__':
    from queue import PriorityQueue

    print(Solution().maxDistance([[1, 0, 1], [0, 0, 0], [1, 0, 1]]))

    print(Solution().maxDistance([[1, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(Solution().maxDistance([[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]))

