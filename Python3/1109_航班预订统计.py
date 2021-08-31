from typing import *


class Solution:
    """ 差分 """
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n
        for left, right, inc in bookings:
            res[left - 1] += inc
            if right < n:
                res[right] -= inc
        for i in range(1, len(res)):
            res[i] += res[i - 1]
        return res
