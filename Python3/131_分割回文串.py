from typing import *


class Solution:
    """回溯法"""

    class Solution:
        def __init__(self):
            self.res = []

        def partition(self, s: str) -> List[List[str]]:
            self.helper(s, [])
            return self.res

        def helper(self, s: str, r: list):
            if s == "":
                self.res.append(r)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    self.helper(s[i:], r + [s[:i]])


class Solution2:
    """回溯法 + 记忆化"""

    def __init__(self):
        self.bp = {}
        self.cache = {}

    def isPalindrome(self, s: str) -> bool:
        if s in self.cache:
            return self.cache[s]
        return s == s[::-1]

    def partition(self, s: str) -> List[List[str]]:
        if s == "":
            return [[]]
        res = []
        for i in range(1, len(s) + 1):
            if self.isPalindrome(s[:i]):
                if s[i:] in self.bp:
                    subs = self.bp[s[i:]]
                else:
                    subs = self.partition(s[i:])
                for sub in subs:
                    res.append([s[:i]] + sub)

                self.bp[s[i:]] = subs
        return res


class Solution3:
    """回溯法 + 动态规划

            动态规划图解
            a       a       b       a     a

        a   a       aa      aab     aaba  aabaa
        a           a       ab      aba   abaa
        b                   b       ba    baa
        a                           a     aa
        a                                 a


    """

    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[True] * len(s) for _ in range(n)]
        cache = {}
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        def helper(start):
            if start >= n:
                return [[]]
            res = []
            for end in range(start, n):
                if dp[start][end]:
                    if end+1 in cache:
                        subs = cache[end+1]
                    else:
                        subs = helper(end + 1)
                    for sub in subs:
                        res.append([s[start:end + 1]] + sub)

                    cache[start] = res
            return res

        return helper(0)


if __name__ == '__main__':
    res = Solution3().partition("aaabaaa")
    print(res)
