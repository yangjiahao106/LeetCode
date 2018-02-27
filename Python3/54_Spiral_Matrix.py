#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/25
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])


class Solution2:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        result = []
        u, d, l, r = 0, len(matrix) - 1, 0, len(matrix[0]) - 1  # 上下左右
        while d > u and r > l:
            for i in range(l, r):  # 注意最后一个不取，消除重复
                result.append(matrix[u][i])
            for i in range(u, d):
                result.append(matrix[i][r])
            for i in range(r, l, -1):
                result.append(matrix[d][i])
            for i in range(d, u, -1):
                result.append(matrix[i][l])
            u, d, l, r = u + 1, d - 1, l + 1, r - 1
        if u == d:
            for i in range(l, r + 1):
                result.append(matrix[u][i])
        elif l == r:
            for i in range(u,d+1):
                result.append(matrix[i][l])
        return result


if __name__ == '__main__':
    so = Solution2()
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    res = so.spiralOrder([[1],[3],[2]])
    print(res)
