#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        p1 = 0
        p2 = len(nums) - 1
        while p2 >= p1:
            if nums[p1] == val:
                while nums[p2] == val and p2 > p1:
                    p2 -= 1
                if p2 == p1:
                    return p1
                nums[p1] = nums[p2]
                p1 += 1
                p2 -= 1
            else:
                p1 += 1
        return p1

class Solution2:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i


if __name__ == '__main__':
    so = Solution()
    res = so.removeElement([2,1,1,3,5],1)
    print(res)