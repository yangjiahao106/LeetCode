from typing import *


class Solution:
    """双指针"""

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        i = 0
        ans = 0
        for house in houses:

            while i < len(heaters) - 1 and abs(heaters[i + 1] - house) <= abs(heaters[i] - house):
                i += 1

            heater = heaters[i]

            ans = max(ans, abs(heater - house))

        return ans


class Solution2:
    """ 二分查找"""

    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        ans = 0
        for house in houses:
            i = self.bisect_right(heaters, house)

            left_distance = house - heaters[i - 1] if i > 0 else float('inf')

            right_distance = heaters[i] - house if i < len(heaters) else float('inf')

            ans = max(ans, min(left_distance, right_distance))

        return ans

    def bisect_right(self, nums: List[int], t):
        l = 0
        r = len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] <= t:
                l = m + 1
            else:
                r = m - 1

        return l


if __name__ == '__main__':
    res = Solution2().findRadius([1, 2, 3, 45, 6, 9, 9], [1, 4, 2, 1])
    print(res)
