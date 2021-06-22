from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in nums:
            res = res ^ i
        return res


class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)
