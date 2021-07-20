from typing import *


class Solution:
    """
    前缀树
    击败 98%
    """

    def __init__(self):
        self.root = {}

    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        for idx, word in enumerate(smalls):
            self.insert(word, idx)

        max_length = max(map(len, smalls))
        res = [[] for i in range(len(smalls))]

        for i in range(len(big)):
            for idx in self.search(big[i:i + max_length]):
                res[idx].append(i)

        return res

    def insert(self, word, idx):
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]

        cur['leaf'] = idx

    def search(self, word) -> []:
        cur = self.root
        res = []
        for c in word:
            if c in cur:
                cur = cur[c]
                if 'leaf' in cur:
                    res.append(cur['leaf'])
            else:
                return res
        return res


import collections


class Solution:
    """
    击败 94%
    """
    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:
        if "" in smalls:
            return [[]]
        if big == "":
            return [[] for i in range(len(smalls))]

        ans = []

        dic = collections.defaultdict(list)
        for i in range(len(big)):
            dic[big[i]].append(i)

        for i, item in enumerate(smalls):

            temp = []
            for j in dic[item[0]]:
                if big[j:j + len(item)] == item:
                    temp.append(j)
            ans.append(temp)
        return ans


class Solution:
    """
    sunday 算法
    超时了
    """

    def multiSearch(self, big: str, smalls: List[str]) -> List[List[int]]:

        res = []
        for small in smalls:
            res.append(self.search(big, small))
        return res

    def search(self, big: str, small: str) -> List[int]:
        big_len = len(big)
        small_len = len(small)
        move = dict()
        for i in range(len(small)):
            move[small[i]] = small_len - i

        s = 0
        res = []

        while s <= big_len - small_len:
            j = 0
            while big[s + j] == small[j]:
                j += 1
                if j >= small_len:
                    res.append(s)
                    break

            if s + small_len >= big_len:
                break

            s += move.get(big[s + small_len], small_len + 1)
        return res


if __name__ == '__main__':
    res = Solution().search("abcabacca", 'c')
    print(res)
