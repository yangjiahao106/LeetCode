from typing import *


class UnionFind:

    def __init__(self):
        self.parent = {}

    def find(self, x):
        root = x
        while self.parent[root] is not None:
            root = self.parent[root]
        if root != x:
            self.parent[x] = root
        return root

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution:
    """225 ms """
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:  # 线的数量最小为 n-1
            return -1

        uf = UnionFind()

        for i in range(n):
            uf.add(i)

        for x, y in connections:
            uf.union(x, y)

        res = 0
        for v in uf.parent.values():
            if v is None:
                res += 1

        return res - 1


class UnionFind2:
    """ 数组代替字典 优化性能"""
    def __init__(self, n):
        self.parent = list(range(n))

    def find(self, x):
        root = x
        while self.parent[root] != root:
            root = self.parent[root]

        if root != x:
            self.parent[x] = root
        return root

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y


class Solution2:
    """ 152 ms """
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:

        if len(connections) < n - 1:  # 线的数量最小为 n-1
            return -1

        uf = UnionFind(n)

        for x, y in connections:
            uf.union(x, y)

        res = 0
        for i, v in enumerate(uf.parent):
            if i == v:
                res += 1

        return res - 1
