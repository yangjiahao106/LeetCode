from typing import *


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        need_count = sum(nums) - x
        if need_count < 0:
            return -1
        if need_count == 0:
            return len(nums)

        length = -1
        l = 0
        count = 0
        for r, n in enumerate(nums):
            count += n
            while l < len(nums) and count >= need_count:
                if count == need_count:
                    if r - l + 1 > length:
                        length = r - l + 1
                count -= nums[l]
                l += 1

        if length == 0:
            return -1
        return len(nums) - length
