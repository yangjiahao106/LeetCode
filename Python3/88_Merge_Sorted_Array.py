#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/12
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        p = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[p] = nums1[m-1]
                p -= 1
                m -= 1
            else:
                nums1[p] = nums2[n-1]
                p -= 1
                n -= 1
        if n > 0:
            nums1[:n] = nums2[:n]
        print(nums1)

if __name__ == '__main__':
    so = Solution()
    so.merge([2,3,0],2,[1],1)