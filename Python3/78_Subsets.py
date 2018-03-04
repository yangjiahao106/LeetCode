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
        # print(path)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, one_res + [nums[i]], res)


class Solution2:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for num in nums:
            res += [each + [num] for each in res]
            # print(res)
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.subsets([1, 2, 3, 4])
    print(res)
