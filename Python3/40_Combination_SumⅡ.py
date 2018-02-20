#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18
class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combinations = []
        self.find(candidates, [], target, combinations)
        return list(set([tuple(l) for l in combinations]))  # 消除重复的值

    def find(self, candidates, res, target, combinations):
        for i, v in enumerate(candidates):
            if v < target:
                self.find(candidates[i + 1:], res + [v], target - v, combinations)
            elif v == target:
                combinations.append(res + [v])
                break


class Solution1_1:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
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


class Solution4:
    def combinationSum2(self, candidates, target):
        # Sorting is really helpful, se we can avoid over counting easily
        candidates.sort()
        result = []
        self.combine_sum_2(candidates, 0, [], result, target)
        return result

    def combine_sum_2(self, nums, start, path, result, target):
        # Base case: if the sum of the path satisfies the target, we will consider
        # it as a solution, and stop there
        if not target:
            result.append(path)
            return

        for i in range(start, len(nums)):
            # Very important here! We don't use `i > 0` because we always want
            # to count the first element in this recursive step even if it is the same
            # as one before. To avoid overcounting, we just ignore the duplicates
            # after the first element.
            if i > start and nums[i] == nums[i - 1]:
                continue

            # If the current element is bigger than the assigned target, there is
            # no need to keep searching, since all the numbers are positive
            if nums[i] > target:
                break

            # We change the start to `i + 1` because one element only could
            # be used once
            self.combine_sum_2(nums, i + 1, path + [nums[i]],
                               result, target - nums[i])


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


if __name__ == '__main__':
    so = Solution1_1()
    res = so.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(res)
