#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/20
class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        O(n)
        space (n)
        """
        #         if len(nums) == 0:
        #             return 1
        #         nums.sort()
        #         for i in range(len(nums)-1):
        #             if nums[i+1] - nums[i] != 1 and nums[i] + 1 > 0:
        #                 return nums[i]+1
        #         return nums[-1] + 1
        nums = set(nums)
        for i in range(1, len(nums) + 2):
            if i not in nums:
                return i


class Solution2:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        将nums的值和nums的下标对应起来，不对应的位置即为所求的值。
        O(n)
        constant space
        """
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                #1.将超过长度的值排除，2.如果该值已经被正确放置，跳过此值，避免死循环
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                # temp = nums[nums[i] - 1]
                # nums[nums[i] - 1] = nums[i]
                # nums[i] = temp

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1


if __name__ == '__main__':
    so = Solution2()
    res = so.firstMissingPositive([3, 4, 3, 1])
    print(res)
