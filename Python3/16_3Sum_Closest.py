#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/8
class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) < 3:
            return []

        dif = abs(nums[0] + nums[1] + nums[2] - target)
        res = nums[0] + nums[1] + nums[2]
        nums.sort()
        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1
            while r > l:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < dif:
                    dif = abs(s - target)
                    res = s
                if s - target > 0:
                    r -= 1
                elif s - target < 0:
                    l += 1
                else:
                    return s
        return res


if __name__ == '__main__':
    so = Solution()
    ret = so.threeSumClosest([-3, -2, -5, 3, -4], -1)
    print(ret)
