from typing import *


class Solution:
    """哈希表、 前缀和 """

    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        s = 0
        ans = 0
        for n in nums:
            s += n
            if s - k in d:
                ans += d[s - k]

            d.setdefault(s, 0)
            d[s] += 1

        return ans
