#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/3
class Solution:
    def subsets(self, nums):
        res = []
        self.dfs(sorted(nums), 0, [], res)
        return res

    def dfs(self, nums, start, one_res, res):
        res.append(one_res)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, one_res + [nums[i]], res)


from typing import *


class Solution2:
    """
    动态规划 击败100%
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for i in nums:
            for j in range(len(res)):
                res.append(res[j] + [i])
        return res


class Solution3:
    """ 位运算 击败 93%"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        for mask in range(2 ** len(nums)):  # 一共 2 ** len(nums) 个结果
            each = []
            for i in range(len(nums)):
                if 1 << i & mask:
                    each.append(nums[i])
            res.append(each)
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.subsets([1, 2, 3, 4])
    print(res)


