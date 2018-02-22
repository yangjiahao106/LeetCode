#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/21
class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        时间复杂度 O(n^3)
        执行超时
        """
        self.res = False
        self.helper(s, p)
        return self.res

    def helper(self, s, p):
        # print('s:', s, 'p:', p)
        if s == '':
            if p.replace('*', '') == '':
                self.res = True
                return
            else:
                return
        elif p == '':
            return
        if p[0] == '?':
            self.helper(s[1:], p[1:])
        elif p[0] == '*':
            self.helper(s[1:], p[1:])
            self.helper(s[1:], p[:])
            self.helper(s[:], p[1:])
        elif p[0] == s[0]:
            self.helper(s[1:], p[1:])


class Solution2:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        动态规划
        """
        dp = [True] + [False] * len(s)

        for i in p:
            if i != '*':
                for n in range(len(s) - 1, 0, -1):
                    dp[n] = dp[n - 1] and (i == s[n] or i == '?')
            else:
                for n in range(1, len(s)):
                    dp[n] = dp[n - 1] or dp[n]
            dp[0] = dp[0] and i == '*'
        return dp[-1]


class Solution3:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        si = 0
        pi = 0
        last_star = -1  # 最后找到的一个 *
        last_star_match = 0  # 最后一个 * 匹配的字符位置

        while si < len(s):
            if pi < len(p) and (s[si] == p[pi] or p[pi] == '?'):
                si += 1
                pi += 1
            elif pi < len(p) and p[pi] == '*':
                last_star_match = si  # * 默认匹配零个字符，si 不变
                last_star = pi
                pi += 1
            elif last_star != -1:  # 如果pi越界 或 p[pi] 与 s[si] 无法匹配
                si = last_star_match + 1  # 则让 * 多匹配一个字符
                pi = last_star + 1
                last_star_match += 1
            else:
                return False

        while pi < len(p) and p[pi] == '*':
            pi += 1
        return pi == len(p)


if __name__ == '__main__':
    so = Solution3()
    res = so.isMatch('abc', '**a*?c*')
    print(res)

    # abddc
    # a*d*c
