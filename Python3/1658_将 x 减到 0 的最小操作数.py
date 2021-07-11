from typing import *


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        need_count = sum(nums) - x  # 将两端的滑块转换成中间的滑块
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


class Solution2:
    def minOperations(self, nums: List[int], x: int) -> int:

        left = len(nums) - 1
        right = len(nums) - 1
        count = sum(nums)
        min_len = float('inf')
        if count < x:
            return -1

        while left >= 0:
            count -= nums[left]
            left -= 1

            while count < x:
                count += nums[right]
                right -= 1

            if count == x:
                if left + len(nums) - right < min_len:
                    min_len = left + len(nums) - right

        if min_len == float('inf'):
            return -1
        return min_len
