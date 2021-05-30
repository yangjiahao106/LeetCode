#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/5
from typing import *


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        超时
        """
        res = 0
        for i, v in enumerate(heights):
            l = r = i
            while l > 0 and heights[l - 1] >= v:
                l -= 1
            while r < len(heights) - 1 and heights[r + 1] >= v:
                r += 1
            width = r - l + 1
            res = max(res, width * v)

        return res


class Solution2:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        参考：https://segmentfault.com/a/1190000007409249
        """
        heights.append(0)  # 补上零，使得最后栈可以全部弹出
        stack = [heights[0]]
        res = 0
        for num in heights[1:]:
            if num >= stack[-1]:  # 如果是升序，进栈
                stack.append(num)
            else:
                count = 1
                while stack and stack[-1] >= num:
                    res = max(res, stack.pop() * count)
                    count += 1

                stack.extend([num] * count)  # 将除栈的元素替换成 num

        return res


class Solution3:
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


if __name__ == '__main__':
    so = Solution2()
    res = so.largestRectangleArea([1])
    print(res)
