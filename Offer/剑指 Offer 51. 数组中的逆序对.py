class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge(nums1, nums2):
            nums3 = []
            i, j = 0, 0
            while i < len(nums1) and j < len(nums2):
                if nums1[i] <= nums2[j]:  # 注意: 相等时不算逆序数对，所以先放入左半部分
                    nums3.append(nums1[i])
                    i += 1
                    res[0] += j  # j 等于 nums2 已放入到 nums3 中的数量， 皆小于 nums1[i], 所以逆序对数 += j
                else:
                    nums3.append(nums2[j])
                    j += 1

            res[0] += len(nums1[i:]) * j
            nums3 += nums1[i:]
            nums3 += nums2[j:]

            return nums3

        def sort(nums):
            if len(nums) == 1:
                return nums

            mid = len(nums) // 2
            left = sort(nums[:mid])
            right = sort(nums[mid:])

            return merge(left, right)

        res = [0]

        sort(nums)
        return res[0]


class Solution(object):
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def merge_sort(l, r) -> int:
            if r - l <= 1:
                return 0
            m = (l + r) // 2
            reverse_count = 0
            reverse_count += merge_sort(l, m)
            reverse_count += merge_sort(m, r)
            tmp = []
            i = l
            j = m
            while i < m and j < r:
                if nums[i] <= nums[j]:  # 注意: 相等时不算逆序数对，所以先放入左半部分, 否则 j 增加后 统计结果会变多
                    tmp.append(nums[i])
                    i += 1
                    reverse_count += (j - m)
                else:
                    tmp.append(nums[j])
                    j += 1

            reverse_count += (j - m) * len(nums[i:m])
            tmp += nums[i:m]
            tmp += nums[j:r]
            nums[l: r] = tmp
            return reverse_count

        return merge_sort(0, len(nums))


if __name__ == '__main__':
    print(Solution().reversePairs([7, 5, 6, 4]))
