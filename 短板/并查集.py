class UnionFind:
    """
    并查集跟树有些类似，只不过她跟树是相反的。
    在树这个数据结构里面，每个节点会记录它的子节点。
    在并查集里，每个节点会记录它的父节点。

    """

    def __init__(self):
        self.parent = {}  # 记录每个节点对应的父节点

    def find(self, x):
        root = x
        # 查找根节点
        while self.parent[root] is not None:
            root = self.parent[root]
        # 路径压缩
        while root != x:
            self.parent[x] = root
            x = self.parent[x]
        return root

    def merge(self, x, y) -> None:
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

    def add(self, x):
        if x not in self.parent:
            self.parent[x] = None

    def is_connect(self, x, y) -> bool:
        return self.find(x) == self.find(y)


from typing import *


class Solution:
    """
    547. 省份数量
    https://leetcode-cn.com/problems/number-of-provinces/
    """

    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        uf = UnionFind()

        for i in range(len(isConnected)):
            uf.add(i)
            for j in range(i):
                if isConnected[i][j]:
                    uf.merge(j, i)

        res = 0
        for v in uf.parent.values():
            if v is None:
                res += 1
        return res


if __name__ == '__main__':
    print(Solution().findCircleNum([[1, 1, 1], [1, 1, 1], [1, 1, 1]]))


