from typing import *
import collections
from math import ceil


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        v2c = collections.Counter(answers)
        res = 0
        for v, count in v2c.items():
            if v == 0:
                res += count
            else:
                res += (v + 1) * ceil(count / (v + 1))
        return res


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        v2c = collections.Counter(answers)
        res = 0
        for v, count in v2c.items():
            res += (count + v) // (v + 1) * (v + 1)  # (count + v) // (v + 1)  向上取整
        return res


