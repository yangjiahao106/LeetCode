#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/14

# 动态规划 经典问题与答案
# http://blog.csdn.net/mrlevo520/article/details/75676160

# 问题一
'''一种双核CPU的两个核能够同时的处理任务，现在有n个已知数据量的任务需要交给CPU处理，
假设已知CPU的每个核1秒可以处理1kb，每个核同时只能处理一项任务。n个任务可以按照
任意顺序放入CPU进行处理，现在需要设计一个方案让CPU处理完这批任务所需的时间最少，
求这个最小的时间。
'''

def doubleCore(work):
    n = sum(work) // 2

    work.add_to_head(0, 0)
    dp = [[0 for _ in range(n + 1)] for _ in range(len(work))]  # 第一行第一列占位

    for i in range(1, len(work)):
        for j in range(1, n + 1):
            if j >= work[i]:
                dp[i][j] = max(dp[i - 1][j], work[i] + dp[i - 1][j - work[i]])
            else:
                dp[i][j] = dp[i - 1][j]

    res = []
    j = n
    for i in range(len(work) - 1, 0, -1):
        if dp[i][j] > dp[i - 1][j]:
            res.append(work[i])
            j -= work[i]

    return res


# 问题二
# 讲DP基本都会讲到的一个问题LIS：longest increasing sub-sequence
# http://www.deeplearn.me/216.html
class Solution:
    def lengthOfLIS(self, nums: [int]) -> int:
        if len(nums) == 0:
            return 0

        d = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j] and d[j] + 1 > d[i]:
                    d[i] = d[j] + 1

        return max(d)


# 问题三
# 最长公共序列：longest common sub-sequence
# 图解地址：http://blog.csdn.net/hrn1216/article/details/51534607
def LCS(l1, l2):
    # test
    # l1 = [3, 5, 7, 4, 8, 6, 7, 8, 2]
    # l2 = [1, 3, 4, 5, 6, 7, 7, 8]

    dp = [[0] * (len(l2) + 1) for i in range(len(l1) + 1)]

    for i in range(1, len(l1) + 1):
        for j in range(1, len(l2) + 1):
            if l1[i - 1] == l2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # print(dp[-1][-1])
    return dp[-1][-1]


# 问题四
# 求连续子数组的最大和
def maxSubString(nums):
    dp = [nums[0]] * len(nums)

    res = nums[0]

    for i in range(1, len(nums)):
        dp[i] = max(dp[i - 1] + nums[i], nums[i])
        res = max(res, dp[i])
    print(res)
    return res



# 问题五
# http://blog.csdn.net/mrlevo520/article/details/75676160
'''给定一个有n个正整数的数组A和一个整数sum,求选择数组A中部分数字和为sum的方案数。 
当两种选取方案有一个数字的下标不一样,我们就认为是不同的组成方案。'''


def allPossibility(nums, target):

    dp = [[1] + [0] * (target) for i in range(len(nums) + 1)]
    print(dp)

    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if nums[i - 1] <= j:
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
            else:
                dp[i][j] = dp[i - 1][j]

    for i in dp:
        print(i)


if __name__ == '__main__':
    allPossibility([5, 5, 10, 2, 3], 10)
