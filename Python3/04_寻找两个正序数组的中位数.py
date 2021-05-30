from typing import *


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = []
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums3.append(nums1[i])
                i += 1
            else:
                nums3.append(nums2[j])
                j += 1
        nums3 += nums1[i:]
        nums3 += nums2[j:]

        if len(nums3) % 2 == 1:
            return nums3[len(nums3) // 2]
        elif len(nums3) > 0:
            return (nums3[len(nums3) // 2] + nums3[len(nums3) // 2 - 1]) / 2
        else:
            return 0
