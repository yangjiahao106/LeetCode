class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        dp = [[0] * n for i in range(n)]
        dp[row][column] = 1

        for i in range(k):
            dp2 = [[0] * n for i in range(n)]
            for row in range(n):
                for col in range(n):
                    if dp[row][col] == 0:
                        continue
                    for x, y in [(-2, -1), (-2, 1), (-1, 2), (1, 2),
                                 (2, 1), (2, -1), (1, -2), (-1, -2)]:
                        row2 = row + x
                        col2 = col + y
                        if 0 <= row2 < n and 0 <= col2 < n:
                            dp2[row2][col2] += (dp[row][col] / 8)

            dp = dp2

        return sum(map(sum, dp))


if __name__ == '__main__':
    print(Solution().knightProbability(3, 1, 0, 0))
