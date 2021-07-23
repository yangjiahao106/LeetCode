#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18


class Solution1_1:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        #深度优先搜索，O()
        """
        candidates.sort()
        all_res = []
        self.find(candidates, 0, [], target, all_res)
        return all_res

    def find(self, candidates, start, res, target, all_res):

        for i in range(start, len(candidates)):
            if candidates[i] < target:
                if i > start and candidates[i] == candidates[i - 1]:  # res同一位置不能有相同的值。
                    continue
                else:
                    self.find(candidates, i + 1, res + [candidates[i]], target - candidates[i], all_res)
            elif candidates[i] == target:
                all_res.append(res + [candidates[i]])
                break


from typing import *


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(path, total, start):
            if total == target:
                res.append(path[:])

            for i in range(start, len(candidates)):
                if total + candidates[i] > target:  # 枝减
                    break
                if i > start and candidates[i] == candidates[i - 1]:  # 防止重复
                    continue  # candidates[i] 会再下一层递归里取到，这个需要跳过它
                path.append(candidates[i])
                dfs(path, total + candidates[i], i + 1)
                path.pop()

        dfs([], 0, 0)
        return res


class Solution3(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        dp = [set() for i in range(target + 1)]
        dp[0].add(())
        for num in candidates:
            for t in range(target, num - 1, -1):
                for prev in dp[t - num]:
                    dp[t].add(prev + (num,))
        return list(dp[-1])


def combinationSum2(self, candidates, target):
    candidates.sort()
    table = [None] + [set() for i in range(target)]
    for i in candidates:
        if i > target:
            break
        for j in range(target - i, 0, -1):
            table[i + j] |= {elt + (i,) for elt in table[j]}
        table[i].add((i,))
    return map(list, table[target])


if __name__ == '__main__':
    so = Solution()
    res = so.combinationSum2([1, 1, 1, 7], 9)
    print(res)
