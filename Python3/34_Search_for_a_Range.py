#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18

class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = self.findStart(nums, 0, len(nums) - 1, target)
        r = self.findEnd(nums, 0, len(nums) - 1, target)
        return [l, r]

    def findStart(self, nums, left, right, target):
        start = -1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target: #如果找到 start等于mid同时Right -= 1
                start = mid
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return start

    def findEnd(self, nums, left, right, target):
        end = -1
        while right >= left:
            mid = (right + left) // 2
            if nums[mid] == target:
                end = mid
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return end


if __name__ == '__main__':
    so = Solution()
    res = so.searchRange([1, 1, 2, 2, 2, 3, 5], 2)
    print(res)
