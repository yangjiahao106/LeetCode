#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/5
class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = nums[0]
        slow = count = 0

        for num in nums:
            if num != temp:
                temp, count = num, 1
            else:
                count += 1

            if count <= 2:
                nums[slow] = num
                slow += 1
        return slow


class Solution2:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for n in nums:
            if i < 2 or n > nums[i - 2]:
                nums[i] = n
                i += 1
        return i


if __name__ == '__main__':
    so = Solution()
    res = so.removeDuplicates([1, 1, 1, 2, 2, 2, 3, 3])
    print(res)
