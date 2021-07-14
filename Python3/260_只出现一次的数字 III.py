from typing import *


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res = 0
        for num in nums: # 先全部异或一遍，通过res 中任意为 1 的位可以将 数字分为两组
            res ^= num

        for i in range(32):
            if res & 1 << i:
                break

        res1 = 0
        res2 = 0

        for num in nums:
            if num & 1 << i:
                res1 ^= num
            else:
                res2 ^= num

        return [res1, res2]