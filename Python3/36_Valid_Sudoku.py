#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/18
class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        return self.isValidRow(board) and \
               self.isValidColumn(board) and \
               self.isValidCube(board)

    def isValidRow(self, board):
        for row in board:
            row = [x for x in row if x != '.']
            if len(row) != len(set(row)):
                return False
        return True

    def isValidColumn(self, board):
        for col in zip(*board):
            col = [x for x in col if x != '.']
            if len(col) != len(set(col)):
                return False
        return True

    def isValidCube(self, board):
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                cube = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3) if board[x][y] != '.']
                if len(cube) != len(set(cube)):
                    return False
        return True


if __name__ == '__main__':
    so = Solution()
    board = [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
             ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
             ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
             ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
             ["9", ".", ".", ".", ".", ".", ".", ".", "."]]
    res = so.isValidSudoku(board)

    print(res)


# class Solution:
#     def isValidSudoku(self, board):
#         return (self.is_row_valid(board) and
#                 self.is_col_valid(board) and
#                 self.is_square_valid(board))
#
#     def is_row_valid(self, board):
#         for row in board:
#             if not self.is_unit_valid(row):
#                 return False
#         return True
#
#     def is_col_valid(self, board):
#         for col in zip(*board):
#             if not self.is_unit_valid(col):
#                 return False
#         return True
#
#     def is_square_valid(self, board):
#         for i in (0, 3, 6):
#             for j in (0, 3, 6):
#                 square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
#                 if not self.is_unit_valid(square):
#                     return False
#         return True
#
#     def is_unit_valid(self, unit):
#         unit = [i for i in unit if i != '.']
#         return len(set(unit)) == len(unit)
