from typing import *


class Solution:
    """
        记忆化递归
    """

    def __init__(self):
        self.not_ok = set()  # 优化性能
        self.res = []

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.helper(s, set(wordDict), "")
        return self.res

    def helper(self, s: str, wordDict: Set, words: str) -> bool:
        if s == "":
            self.res.append(words[1:])
            return True

        if s in self.not_ok:
            return False

        b = False
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if self.helper(s[i:], wordDict, words + " " + s[:i]):
                    b = True

        if not b:
            self.not_ok.add(s)

        return b


class Solution3:
    """
        记忆化递归
    """

    def __init__(self):
        self.bp = {}

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = self.helper(s, set(wordDict))
        print(len(self.bp))
        return [" ".join(words) for words in res]

    def helper(self, s: str, wordDict: Set) -> List[List[str]]:
        if s == "":
            return [[]]

        ans = []
        for i in range(len(s) + 1):
            if s[:i] in wordDict:
                if s[i:] in self.bp:
                    ans2 = self.bp[s[i:]]
                else:
                    ans2 = self.helper(s[i:], wordDict)
                for a in ans2:
                    ans.append([s[:i]] + a)

        self.bp[s] = ans
        return ans


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def backtrack(path, s):
            if len(s) == 0:
                res.append(path[1:])  # 第一个是空格
                return

            for leng in range(1, len(s) + 1):
                strs = s[:leng]
                if strs in wordDict:
                    backtrack(path + ' ' + strs, s[leng:])
            return

        res = []
        backtrack('', s)
        return res


if __name__ == '__main__':
    import datetime

    t1 = datetime.datetime.now().timestamp()
    print(t1)
    res = Solution3().wordBreak("aaaaaaaaaaaaaaaaaaaaaa", ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"])
    t2 = datetime.datetime.now().timestamp()
    print(t2 - t1)
    print(len(res), len(set(res)))
