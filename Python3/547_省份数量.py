from typing import *

from collections import deque


class Solution:
    """BFS"""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if len(isConnected) == 0:
            return 0

        length = len(isConnected[0])

        visited = [False] * length

        res = 0
        q = deque()
        for i in range(length):

            if visited[i]:
                continue

            res += 1

            q.append(i)
            visited[i] = True

            while q:
                a = q.popleft()
                for b in range(length):
                    if not visited[b] and isConnected[a][b]:
                        visited[b] = True
                        q.append(b)

        return res


class Solution:
    """DFS"""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(a):
            visited[a] = True
            for b in range(length):
                if not visited[b] and isConnected[a][b]:
                    dfs(b)

        length = len(isConnected[0])
        visited = [False] * length
        res = 0
        for i in range(length):
            if not visited[i]:
                res += 1
                dfs(i)
        return res


class Solution:
    """ 并查集"""

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def find(index: int) -> int:
            if parent[index] != index:
                parent[index] = find(parent[index])

            return parent[index]

        def union(index1: int, index2: int):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles


if __name__ == '__main__':
    c = [[1, 0, 0, 1],
         [0, 1, 1, 0],
         [0, 1, 1, 1],
         [1, 0, 1, 1]]
    print(Solution().findCircleNum(c))
