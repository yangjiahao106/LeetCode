from typing import *


class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        d = dict()
        max_length = 0
        for num in nums:
            if num not in d:
                left = d.get(num - 1, 0)
                right = d.get(num + 1, 0)
                length = left + right + 1
                if length > max_length:
                    max_length = length
                d[num] = length
                d[num - left] = length  # 更新左边界
                d[num + right] = length  # 更新右边界
        return max_length


class Solution:
    def longestConsecutive(self, nums):
        '''
        相等的数字不会增长序列长度，但也不会中断序列的统计；使用set集合，去除重复数字；
        对于一个nums_set 集合， 要判段最长的连续序列，那么就得依次找左边界和右边界
        [1,3,2,8,4,5,8,9]
        假设以1为左边界，给定循环每次加1 判断2 是否在nums_set 3 是否在nums_set 依次统计到5，6不在，因此此时的连续序列长度左边界1 右边界5 长度4；
        然后以3为左边界的时候，又会统计到5；这样会多次遍历已经寻找过的数字，从而造成冗余和时间消耗

        此处寻找当前元素的前一个元素是否在集合中，减少冗余

        当数组为有序数组，且间隔为1时，如[1,2,3,4,5]，此时内部循环while会遍历N次，外部循环则会空转N-1次；时间上则是O(N)+O(N-1),平均复杂度则为O(N)；

        '''
        longest_streak = 0
        # 去重
        num_set = set(nums)
        # 依次遍历集合的set
        for num in num_set:
            # 只有当该元素的前一个元素 不在set中，代表是一个新序列的左边界
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                # 以此元素为左边界，依次增加大小，，并且判断是否在set中，这样可以获得集合的右边界
                while current_num + 1 in num_set:
                    current_num += 1
                    # 记录当前序列的最大长度
                    current_streak += 1
                # 当前序列的长度与最大长度比较取最大
                longest_streak = max(longest_streak, current_streak)

        return longest_streak