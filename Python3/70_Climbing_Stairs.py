#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1:
            return 1
        dp = [1, 1]

        for i in range(n - 1):
            dp.append(dp[-1] + dp[-2])

        return dp[-1]


class Solution2:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = b = 1
        for i in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == '__main__':
    so = Solution2()
    res = so.climbStairs(4)
    print(res)
