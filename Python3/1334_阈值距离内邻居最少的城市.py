from typing import *


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, d in edges:
            dist[i][j] = d
            dist[j][i] = d

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        res = 0
        minC = float('inf')
        for i in range(n):
            c = 0
            for j in range(n):
                if dist[i][j] <= distanceThreshold:
                    c += 1
            if c <= minC:
                minC = c
                res = i
        return res
