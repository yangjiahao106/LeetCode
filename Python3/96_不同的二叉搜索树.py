class Solution:
    """记忆化递归"""

    def numTrees(self, n: int) -> int:
        bp = {}

        def helper(l, r):
            if l >= r: return 1
            if (l, r) in bp:
                return bp[(l, r)]
            res = 0
            for i in range(l, r):
                res += (helper(l, i) * helper(i + 1, r))
            bp[(l, r)] = res
            return res

        return helper(0, n)


class Solution:
    """动态规划"""

    def numTrees(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1  # 零个元素 有一种组合方式

        for i in range(1, n + 1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i - j - 1]  # 左边的数量 * 右边的数量

        return dp[-1]
