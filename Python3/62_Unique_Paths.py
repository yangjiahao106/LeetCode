#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/28
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1, 1]]
        while True:
            temp = []
            flag = False
            for l in dp:
                if l[0] < m:
                    temp.append([l[0] + 1, l[1]])
                    flap = True
                if l[1] < n:
                    temp.append([l[0], l[1] + 1])
                    flag = True
                if l[0] == m and l[1] == n:
                    temp.append(l)
            dp = temp
            if flag == False:
                return len(dp)


class Solution2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1] * n for i in range(m)]  # 第一行，和第一列需要初始化为1

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j]

        return dp[-1][-1]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * (n + 1) for i in range(m + 1)]
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:  # 起始位置设为1
                    dp[row][col] = 1
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[-1][-1]


if __name__ == '__main__':
    so = Solution2()
    res = so.uniquePaths(2, 2)
    print(res)
