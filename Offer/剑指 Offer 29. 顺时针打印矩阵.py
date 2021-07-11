from typing import *


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        def helper(row, col):
            res = []

            for i in range(col, cols - col):
                res.append(matrix[row][i])

            if row == rows - row - 1:  # 列长度为1，说明只剩一行了需要返回， 否则从右边往左打印后会重复
                return res

            for i in range(row + 1, rows - row ):
                res.append(matrix[i][cols - col - 1])

            if col == cols - col - 1:  # 行长度为1 所以只剩一列了:
                return res

            for i in range(cols - col - 2, col, -1):
                res.append(matrix[rows - row - 1][i])

            for i in range(rows - row - 1, row, -1):
                res.append(matrix[i][col])
            return res

        rows = len(matrix)
        cols = len(matrix[0])
        row = 0
        col = 0
        res = []
        while row * 2 < len(matrix) and col * 2 < len(matrix[0]):  # 注意如果用 row  < len(matrix)// 2 奇数行时会少打印
            res += helper(row, col)
            row += 1
            col += 1
        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        # 初始化边界
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while 1:
            # 在这四次遍历中，任意一次出现上下或左右边界发生触碰的情况，就说明已经把所有的值都遍历完了，直接跳出循环
            # 从左向右
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1
            if t > b:
                break

                # 从上到下
            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break

            # 从右到左
            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            if b < t:
                break

            # 从下到上
            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res

if __name__ == '__main__':
    print(Solution().spiralOrder([[3],[2]]))
    print(Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
