#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combinations = []
        self.find(candidates, [], target, combinations)
        return combinations

    def find(self, candidates, res, target, combinations):
        for i, v in enumerate(candidates):
            if v < target:
                self.find(candidates[i:], res + [v], target - v, combinations)
            elif v == target:
                combinations.append(res + [v])
                break


from typing import *


class Solution2:
    """ 击败 99%"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        length = len(candidates)
        candidates.sort()  # 排序 方便枝减

        def dfs(path, s, start):
            if s == target:
                res.append(path[:])

            for i in range(start, length):
                if s + candidates[i] > target:  # 枝减
                    break
                path.append(candidates[i])
                dfs(path, s + candidates[i], i)
                path.pop()

        dfs([], 0, 0)
        return res


if __name__ == '__main__':
    pass

