#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/5

class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        深度优先搜索
        """
        if not board: return False
        if not word: return True

        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, word, i, j):
                    return True
        return False

    def helper(self, board, word, i, j):
        if board[i][j] == word[0]:
            if len(word) == 1:
                return True  # 只有一个单词且相等。

            board[i][j] = ' '  # 一个单词只能使用一次,避免重复使用

            if i > 0 and self.helper(board, word[1:], i - 1, j):
                return True
            if i < len(board) - 1 and self.helper(board, word[1:], i + 1, j):
                return True
            if j > 0 and self.helper(board, word[1:], i, j - 1):
                return True
            if j < len(board[0]) - 1 and self.helper(board, word[1:], i, j + 1):
                return True

            board[i][j] = word[0]  # 如果找不到要把单词放回原处。
            return False
        else:
            return False


if __name__ == '__main__':
    so = Solution()
    res = so.exist([['A'], ], 'A')
    print(res)
