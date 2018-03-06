#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/5
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        start, end = 0, len(nums) - 1

        while end >= start:
            mid = (start + end) // 2
            if nums[mid] == target:
                return True
            # 重点。
            while start < mid and nums[start] == nums[mid]:  # tricky part
                start += 1

            if nums[mid] >= nums[start]:  # 左侧升序。
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1

            else:  # 右侧升序
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
        return False


if __name__ == '__main__':
    so = Solution()
    res = so.search([1, 3, 1, 1, 1], 3)
    print(res)
