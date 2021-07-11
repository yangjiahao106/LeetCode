from typing import *


class Solution:
    """正常递归"""

    def __init__(self):
        self.res = 1 << 32 - 1

    def minSideJumps(self, obstacles: List[int]) -> int:

        def helper(obstacles, n, count):
            if len(obstacles) <= 1:
                self.res = min(self.res, count)
                return

            if obstacles[1] != n:
                helper(obstacles[1:], n, count)
            else:
                for n2 in [1, 2, 3]:
                    if n2 == n:
                        continue
                    if obstacles[0] == n2:
                        continue
                    helper(obstacles, n2, count + 1)

        helper(obstacles, 2, 0)
        return self.res


class Solution:
    """记忆化递归"""

    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = {}

        def helper(start, n) -> int:
            if start == len(obstacles) - 2:
                return 0
            if (start, n) in dp:
                return dp[(start, n)]

            count = 1 << 32
            if obstacles[start + 1] != n:
                count = helper(start + 1, n)

            else:
                for n2 in [1, 2, 3]:
                    if n2 == n:
                        continue
                    if obstacles[start] == n2:
                        continue
                    count = min(count, helper(start + 1, n2) + 1)

            dp[(start, n)] = count
            return count

        return helper(0, 2)


class Solution:
    """动态规划"""

    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [[float("inf")] * 4 for _ in range(len(obstacles))]
        dp[0] = [0, 1, 0, 1]

        for pos in range(1, len(obstacles)):
            for line in [1, 2, 3]:
                if obstacles[pos - 1] != line:
                    dp[pos][line] = dp[pos - 1][line]
                else:
                    for sideLine in [1, 2, 3]:
                        if sideLine == line:
                            continue
                        if obstacles[pos] != sideLine and obstacles[pos - 1] != sideLine:
                            dp[pos][line] = min(dp[pos][line], dp[pos - 1][sideLine] + 1)
        return min(dp[-1])


class Solution:
    "贪心算法"

    def minSideJumps(self, obstacles: List[int]) -> int:
        count = 0
        pos = 0
        line = 2
        while pos < len(obstacles) - 1:
            while pos < len(obstacles) - 1 and obstacles[pos + 1] != line:
                pos += 1
            if pos < len(obstacles) - 1:
                maxSkip = 0
                maxSkipLine = 0
                for nextLine in [1, 2, 3]:
                    if line == nextLine or obstacles[pos] == nextLine:
                        continue
                    skip = 0
                    while pos + skip < len(obstacles) - 1 and obstacles[pos + skip + 1] != nextLine:
                        skip += 1
                    if skip > maxSkip:
                        maxSkipLine = nextLine
                        maxSkip = skip

                count += 1
                pos += maxSkip
                line = maxSkipLine

        return count


if __name__ == '__main__':
    # print(Solution().minSideJumps([0, 2, 1, 0, 3, 0]))
    print(Solution().minSideJumps([0, 1, 1, 3, 3, 0]))

    from functools import lru_cache
