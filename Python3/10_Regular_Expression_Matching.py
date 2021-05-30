#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/3

class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s

        fir_match = bool(s) and (p[0] in ['.', s[0]])

        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or fir_match and self.isMatch(s[1:], p[:])
        else:
            return fir_match and self.isMatch(s[1:], p[1:])

    def isMatch2(self, s, p):
        m = len(s)
        n = len(p)
        dp = [[True] + [False] * m]
        for i in range(n):
            dp.append([False] * (m + 1))

        for i in range(1, n + 1):
            x = p[i - 1]
            if x == '*' and i > 1:
                dp[i][0] = dp[i - 2][0]
            for j in range(1, m + 1):
                if x == '*':
                    dp[i][j] = dp[i - 2][j] or dp[i - 1][j] or (dp[i - 1][j - 1] and p[i - 2] == s[j - 1]) or (
                            dp[i][j - 1] and p[i - 2] == '.')
                elif x == '.' or x == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]

        return dp[n][m]


class Solution2(object):
    def isMatch(self, s, p, memo={("", ""): True}):
        if not p and s:      return False
        if not s and p:      return set(p[1::2]) == {"*"} and not (len(p) % 2)
        if (s, p) in memo:    return memo[s, p]

        char, exp, prev = s[-1], p[-1], 0 if len(p) < 2 else p[-2]
        memo[s, p] = \
            (exp == '*' and ((prev in {char, '.'} and self.isMatch(s[:-1], p, memo)) or self.isMatch(s, p[:-2], memo))) \
            or \
            (exp in {char, '.'} and self.isMatch(s[:-1], p[:-1], memo))
        return memo[s, p]


if __name__ == '__main__':
    so = Solution()
    ok = so.isMatch("aa", ".*")
    print(ok)
