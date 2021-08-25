from typing import *


class Solution:
    # [2,1,5,6,2,3]
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                w = i - stack[-1]
                h = heights[stack.pop()]
                res = max(res, w * h)

            stack.append(i)

        return res

