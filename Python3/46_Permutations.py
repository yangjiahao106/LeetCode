#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/22

class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        dp = [[]]
        for num in nums:
            temp = []
            for li in dp:
                for pos in range(len(li) + 1):
                    temp.append(li[:pos] + [num] + li[pos:])
            dp = temp
        return dp


from typing import *


class Solution2:
    """
    递归


    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return [nums]

        res = []
        for i in range(len(nums)):
            # 先取出其中一个数字， 然后递归求解子问题，让后将取出来的数字放入到子问题的结果中
            subs = self.permute(nums[:i] + nums[i + 1:])
            for sub in subs:
                sub.append(nums[i])
                res.append(sub)
        return res


class Solution3:
    """递归"""

    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path, used):

            if len(path) == len(nums):
                res.append(path)
                return

            for n in nums:
                if n not in used:
                    used.add(n)
                    dfs(path + [n], used)
                    used.remove(n)

        res = []

        dfs([], used=set())

        return res


if __name__ == '__main__':
    so = Solution3()
    res = so.permute([1, 2, 3])
    print(res)
