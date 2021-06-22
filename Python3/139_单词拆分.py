from typing import *


class Solution:
    """
        递归回溯法 超时了
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if self.wordBreak(s[i:], wordDict):
                    return True

        return False


class Solution:
    """
        记忆化递归
    """

    def __init__(self):
        self.not_ok = set()  # 优化性能

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.helper(s, set(wordDict))

    def helper(self, s: str, wordDict: Set) -> bool:
        if s == "":
            return True
        if s in self.not_ok:
            return False
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if self.helper(s[i:], wordDict):
                    return True

        self.not_ok.add(s)
        print(len(self.not_ok))
        return False


class Solution3:
    """
        动态规划
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(0, len(dp)-1):
            for j in range(i + 1, len(dp)):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True

        return dp[-1]


if __name__ == '__main__':
    print(Solution3().wordBreak("applepenapple",
                                ["apple", "pen"]))
