#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/6

from typing import *


class Solution:
    """ 暴力算法 """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:

        def helper(row, colA, colB):
            m = (colB - colA + 1)
            for row2 in range(row + 1, len(matrix)):
                all1 = True
                for c in range(colA, colB + 1):
                    if matrix[row2][c] == "0":
                        all1 = False
                        break
                if all1:
                    m += (colB - colA + 1)
                else:
                    break
            return m

        res = 0
        for row in range(0, len(matrix)):
            for col in range(0, len(matrix[0])):
                if matrix[row][col] == "0":
                    continue

                for col2 in range(col, len(matrix[0])):
                    if matrix[row][col2] == "0":
                        break
                    m = helper(row, col, col2)
                    res = max(res, m)

        return res


class Solution2:
    """ 单调栈 """

    # 根据高度求最大面积 参考 leetCode:  84. 柱状图中最大的矩形

    def getMaxAreaWighHeights(self, heights):

        heights = [0] + heights + [0]
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] - 1
                ans = max(ans, h * w)
            stack.append(i)

        # print(heights, ans)
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        ans = 0
        heights = [0] * len(matrix[0])

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heights[j] = heights[j] + 1 if matrix[i][j] == "1" else 0

            ans = max(ans, self.getMaxAreaWighHeights(heights))
        return ans


if __name__ == '__main__':
    so = Solution2()
    res = so.maximalRectangle([["1", "0", "1", "0", "0"],
                               ["1", "0", "1", "1", "1"],
                               ["1", "1", "1", "1", "1"],
                               ["1", "0", "0", "1", "0"]])
    print(res)
    res = so.maximalRectangle([["0", "1"], ["1", "0"]])
    print(res)
