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


class Solution2:
    """
        核心思路是对于数组中的每一个数字找到第一个小于它的数字，这种问题一般需要使用单调栈

    """

    def largestRectangleArea(self, heights: List[int]) -> int:
        # 单调栈 + 常数优化
        n = len(heights)
        if n == 0:
            return 0

        stack = []

        left, right = [0] * n, [0] * n

        for i in range(n):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            left[i] = stack[-1] if stack else -1

            stack.append(i)

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()

            right[i] = stack[-1] if stack else n
            stack.append(i)

        res = max((right[i] - left[i] - 1) * heights[i] for i in range(n))
        return res


if __name__ == '__main__':
    pass
