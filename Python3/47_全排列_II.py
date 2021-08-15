#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/22

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        #基于permutations 1 使用set进行去重。
        """
        dp = {()}
        for num in nums:
            temp = set()
            for li in dp:
                for pos in range(len(li) + 1):
                    temp.add(li[:pos] + (num,) + li[pos:])
            dp = temp
        return list(dp)


class Solution2:
    def permuteUnique(self, nums):
        """
        [1,1, 2, 2] 递归树↓（部分）

                        1
                  1     2     2
                 2 2   1 2   1  2
                2   2 2   1 2    1

                        1
                  1     2     2
                 2 2   1 2   1  2
                2   2 2   1 2    1

        """

        all_result = []
        nums.sort()
        self.helper([], nums, all_result)
        return all_result

    def helper(self, result, rest, all_results):
        if rest == []:
            return all_results.append(result)
        for i, v in enumerate(rest):
            if i > 0 and rest[i] == rest[i - 1]:  # 如果和上一个值相同则不能在这一层被再次选中了，但可以在下一层递归里被使用
                continue
            self.helper(result + [v], rest[:i] + rest[i + 1:], all_results)  #


from typing import *


class Solution2:
    """ 动态规划"""

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dp = [[]]

        for i in range(len(nums)):
            dp2 = []

            for path in dp:
                for start in range(len(path) + 1):
                    dp2.append(path[:start] + [nums[i]] + path[start:])
                    if start < len(path) and path[start] == nums[i]:
                        break  # 重点
            dp = dp2
        return dp


if __name__ == '__main__':
    so = Solution2()
    res = so.permuteUnique([1, 2, 2, 1])
    print(res)
