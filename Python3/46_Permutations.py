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


if __name__ == '__main__':
    so = Solution()
    res = so.permute([1, 2, 3])
    print(res)
