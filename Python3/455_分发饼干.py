from typing import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i = 0
        for n in s:
            if n >= g[i]:
                i += 1
                if i == len(g):
                    return i
        return i

