from typing import *

""" """


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def count(n):
            c = 0
            while n:
                n &= n - 1  # 每次把最低为的1变成0
                c += 1
            return c

        res = []
        for i in range(12):
            for j in range(60):
                if count(i) + count(j) == turnedOn:
                    res.append("%d:%02d" % (i, j))

        return res


def count(n):
    """ 计算二进制中1 的数量"""
    c = 0
    while n:
        n &= n - 1  # 每次把最低为的1变成0
        c += 1
    return c


if __name__ == '__main__':
    print(Solution().readBinaryWatch(1))
