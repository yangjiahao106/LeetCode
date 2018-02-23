#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/23
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()

        for row in range(len(matrix)): # 转置
            for col in range(row, len(matrix[0])):
                to_row = col
                to_col = row
                # print(to_row, to_col)
                matrix[to_row][to_col], matrix[row][col] = matrix[row][col], matrix[to_row][to_col]

        return matrix

class Solution2(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])

if __name__ == '__main__':
    so = Solution()
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    res = so.rotate([[1,2],[3,4]])
    print(res)
