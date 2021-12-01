#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/8
class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
        return res


from typing import *


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]: continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                if l > i + 1 and nums[l] == nums[l - 1]:
                    l += 1
                    continue

                if r < len(nums) - 1 and nums[r] == nums[r + 1]:
                    r -= 1
                    continue

                if nums[i] + nums[l] + nums[r] == 0:
                    res.append((nums[i], nums[l], nums[r]))

                if nums[l] + nums[r] > - nums[i]:
                    r -= 1
                else:
                    l += 1
        return res

if __name__ == '__main__':
    so = Solution()
    ret = so.threeSum([-5, -1, -1, 0, 1, 2, 3, 4])
    print(ret)
