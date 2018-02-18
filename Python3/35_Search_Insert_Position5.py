#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18

class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while end >= start:
            mid = (end + start) // 2
            if nums[mid] >= target:
                end = mid - 1
            else:
                start = mid + 1
        # print(start, end )
        return start


if __name__ == '__main__':
    so = Solution()
    res = so.searchInsert([1,2,4,5], 3)
    print(res)
