#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.remove(nums[i])
                i -= 1
            i += 1

        return nums


class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        i = 0
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            else:
                pass
        return i + 1


if __name__ == '__main__':
    li = [1,1,2]
    so = Solution2()
    res = so.removeDuplicates(li)
    print(res)
