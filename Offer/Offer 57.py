from typing import *


class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # 双指针

        l, r = 1, 2
        ans = []
        while l < r:
            sum = (l + r) * (r - l + 1) // 2

            if sum == target:
                ans.append([i for i in range(l, r)])
                l += 1
            elif sum > target:
                l += 1
            else:
                r += 1
        return ans
