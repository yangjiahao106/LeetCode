#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/10
import copy


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        original = copy.copy(nums)
        nums.sort()

        left = 0
        right = len(nums) - 1

        while right > left:
            if nums[left] + nums[right] < target:
                left += 1
            elif nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] == target:
                print(nums[left], nums[right])
                print(original)
                return [original.index(nums[left]) + 1, original.index(nums[right]) + 1]
        return None


class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, v in enumerate(nums):
            number = target - v
            if number in nums[i + 1:]:
                index = nums.index(number)
                return [i + 1, index + 1]
        return None


if __name__ == '__main__':
    so = Solution2()
    li = so.twoSum([3, 2, 4], 6)
    print(li)
