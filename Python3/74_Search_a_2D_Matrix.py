#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/2
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        时间复杂度 O(m + n)
        """
        if not matrix:
            return False
        row = 0
        col = len(matrix[0]) - 1
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1
        return False


if __name__ == '__main__':
    so = Solution()
    res = so.searchMatrix([[-10,-8,-6,-4,-3],[0,2,3,4,5],[8,9,10,10,12]], 0)
    print(res)