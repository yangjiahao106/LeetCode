#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/26

class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        从前往后
        时间负责度O(n)
        """
        furthest = 0
        for i, v in enumerate(nums):
            if i > furthest:
                return False
            furthest = max(furthest, i + v)
        return True


class Solution2:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        从后往前
        """
        goal = len(nums) - 1
        for i in range(len(nums), -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return not goal


if __name__ == '__main__':
    so = Solution()
    res = so.canJump([1, 2, 0, 0, 0])
    print(res)
