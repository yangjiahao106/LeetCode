#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/22
class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        # 贪婪算法
        """
        if len(nums) <= 0:
            return 0
        jump = step = 0
        pos = 0
        while pos + nums[pos] < len(nums) - 1:
            farthest = 0
            for j in range(1, nums[pos] + 1):
                if (j + nums[pos + j]) > farthest:
                    farthest = j + nums[pos + j]
                    step = j
            pos += step
            jump += 1

        return jump + 1

if __name__ == '__main__':
    so = Solution()
    res = so.jump([])
    print(res)
