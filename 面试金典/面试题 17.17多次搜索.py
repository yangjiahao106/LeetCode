from typing import *


class Solution:

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
