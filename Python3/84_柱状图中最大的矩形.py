from typing import *


class Solution:
    """ 单调栈 """

    # [2,1,5,6,2,3]
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        res = 0
        for i in range(len(heights)):
            while len(stack) > 0 and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                res = max(res, h * w)
            stack.append(i)
        return res


pass
