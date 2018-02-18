#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i + 1] > nums[i]:
                for j in range(len(nums) - 1, 0, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        self.reverse(nums, i + 1)  # 翻转后面的增序数字，使其构成的数字最小。
                        return

        self.reverse(nums, 0)
        # print(nums)

    def reverse(self, nums, start):
        end = len(nums) - 1
        while end > start:
            nums[end], nums[start] = nums[start], nums[end]
            end -= 1
            start += 1


if __name__ == '__main__':
    so = Solution()
    so.nextPermutation([4, 3, 2, 1])
