from typing import *


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:

        lengths = [1] * len(nums)
        counts = [1] * len(nums)
        max_length = 1

        for right in range(len(nums)):
            for left in range(0, right):
                if nums[right] > nums[left]:

                    if lengths[left] + 1 > lengths[right]:
                        lengths[right] = lengths[left] + 1
                        counts[right] = counts[left]  # 长度增加了，数量等于之前的数量

                    elif lengths[left] + 1 == lengths[right]:  # 出现了长度一样的情况
                        counts[right] += counts[left]

                    max_length = max(max_length, lengths[right])

        # print(lengths)
        # print(counts)

        res = 0
        for i in range(len(nums)):
            if lengths[i] == max_length:
                res += counts[i]
        return res


if __name__ == '__main__':
    print(Solution().findNumberOfLIS([1, 3, 5, 4, 7, 2, 3, 4, 5,6]))
