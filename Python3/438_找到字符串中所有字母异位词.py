from typing import *


class Solution:
    "时间复杂度 n * m"

    def findAnagrams(self, s: str, p: str) -> List[int]:
        m = [0] * 26
        for c in p:
            m[ord(c) - ord('a')] += 1

        p_length = len(p)

        res = []
        for l in range(len(s) - p_length + 1):
            tmp = m[:]
            for i in range(l, l + p_length):
                if tmp[ord(s[i]) - ord('a')] <= 0:
                    break
                else:
                    tmp[ord(s[i]) - ord('a')] -= 1

                if i == l + p_length - 1:
                    res.append(l)

        return res


class Solution:
    "时间复杂度 n * 26 = n"

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        m_s = [0] * 26
        m_p = [0] * 26

        for i in range(len(p)):
            m_s[ord(s[i]) - ord('a')] += 1
            m_p[ord(p[i]) - ord('a')] += 1

        res = []
        if m_s == m_p:
            res.append(0)

        for i in range(len(p), len(s)):
            m_s[ord(s[i]) - ord('a')] += 1
            m_s[ord(s[i - len(p)]) - ord('a')] -= 1
            if m_s == m_p:
                res.append(i)

        return res
