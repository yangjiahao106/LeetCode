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
                combinations.append(res+[v])
                break

if __name__ == '__main__':
    pass