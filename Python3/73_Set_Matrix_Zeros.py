#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/2
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        空间复杂度 O(m + n)
        """
        m = len(matrix)
        n = len(matrix[0])

        row, col = [], []

        for r in range(m):
            for c in range(n):
                if matrix[r][c] == 0:
                    row.append(r)
                    col.append(c)

        for r in row:
            for i in range(n):
                matrix[r][i] = 0

        for c in col:
            for i in range(m):
                matrix[i][c] = 0


class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        空间复杂度 O(m + n) 利用第一行和第一列作为标记
        """
        m = len(matrix)
        n = len(matrix[0])
        first_row_has_zero = not all(matrix[0])  # 记录第一行是否有零

        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 0:  # 找出除了一行一列外，所有的零并在所在行和列左标记
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            for j in range(n - 1, -1, -1):  # 从后往前遍历，第一列需要最后判断
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0  #

        if first_row_has_zero:
            for i in range(n):
                matrix[0][i] = 0

        # print(matrix)


if __name__ == '__main__':
    so = Solution2()
    so.setZeroes([[0, 0, 0, 5], [4, 3, 1, 4], [0, 1, 1, 4], [1, 2, 1, 3], [0, 0, 1, 1]])
