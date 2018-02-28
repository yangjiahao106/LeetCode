#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/27
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        matrix = [[0] * n for i in range(n)]
        start, end = 0, n - 1
        step = 1
        while end > start:
            for i in range(start, end):
                matrix[start][i] = step
                step += 1
            for i in range(start, end):
                matrix[i][end] = step
                step += 1
            for i in range(end, start, -1):
                matrix[end][i] = step
                step += 1
            for i in range(end, start, -1):
                matrix[i][start] = step
                step += 1
            start, end = start + 1, end - 1
        if start == end:
            matrix[start][end] = step
        return matrix


if __name__ == '__main__':
    so = Solution()
    res = so.generateMatrix(2)
    for i in res:
        print(i)
