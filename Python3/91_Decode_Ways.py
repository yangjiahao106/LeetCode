#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13
class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [1]
        dp.append(1 if s[0] != '0' else 0)
        for i in range(1, len(s)):
            if s[i] == '0':
                if 0 < int(s[i - 1:i + 1]) <= 26:
                    dp.append(dp[-2])
                else:
                    dp.append(0)
            else:
                if 10 < int(s[i - 1:i + 1]) <= 26:
                    dp.append(dp[-1] + dp[-2])
                else:
                    dp.append(dp[-1])
        return dp[-1]


class Solution2:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s) == 0:
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            t1 = int(s[i - 1:i])
            t2 = int(s[i - 2:i])
            if (t1 >= 1 and t1 <= 9):
                dp[i] += dp[i - 1]
            if (t2 >= 10 and t2 <= 26):
                dp[i] += dp[i - 2]

        return dp[len(s)]


if __name__ == '__main__':
    so = Solution()
    res = so.numDecodings('01')
    print(res)
