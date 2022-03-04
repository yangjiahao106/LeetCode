from typing import *


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums.sort()
        zero_count = nums.count(0)
        interval = 0
        for i in range(zero_count, len(nums) - 1):
            interval += (nums[i + 1] - nums[i] - 1)

        return interval <= zero_count


if __name__ == '__main__':
    print(Solution().isStraight([0, 0,0, 1, 5, 6]))
