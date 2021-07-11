class Solution:
    def totalNQueens(self, n: int) -> int:
        return self.helper(n, 0, set())

    def canPut(self, n, row, col, queenSet) -> bool:
        # 左上,  上， 右上 方向上递归
        for i in range(row):  # 上
            if (i, col) in queenSet:
                return False

        for i in range(1, min(row, col) + 1):  # 左上
            if (row - i, col - i) in queenSet:
                return False

        for i in range(1, min(row, n - col - 1) + 1):  # 右上
            if (row - i, col + i) in queenSet:
                return False
        return True

    def helper(self, n, row, queenSet: set):
        count = 0
        for col in range(n):
            if self.canPut(n, row, col, queenSet):
                if row == n - 1:
                    count += 1
                    continue
                queenSet.add((row, col))
                count += self.helper(n, row + 1, queenSet)
                queenSet.remove((row, col))
        return count


class Solution2:
    def totalNQueens(self, n: int) -> int:
        def helper(row):
            if row == n:
                return 1
            count = 0
            for col in range(n):
                if col in columns or col + row in diagonal1 or col - row in diagonal2:
                    continue
                columns.add(col)
                diagonal1.add(col + row)
                diagonal2.add(col - row)
                count += helper(row + 1)
                columns.remove(col)
                diagonal1.remove(col + row)
                diagonal2.remove(col - row)
            return count

        columns = set()  # 列
        diagonal1 = set()  # 对角线 左下右上
        diagonal2 = set()  # 对角线 左上右下

        return helper(0)


if __name__ == '__main__':
    print(Solution2().totalNQueens(5))
