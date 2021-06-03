class Solution:
    """
      m i t c m u
    m 1 1 1 1 1 1
    t 1 1 2 2 2 2
    a 1 1 2 2 2 2
    c 1 1 2 3 3 3
    n 1 1 2 3 3 3
    u 1 1 2 3 3 4
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * (len(text2) + 1) for i in range(len(text1) + 1)]

        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + 1
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], dp[i][j])


        return dp[-1][-1]


if __name__ == '__main__':
    # "bsbininm"
    # "jmjkbkjkv"
    print(Solution().longestCommonSubsequence("bsbininm", "jmjkbkjkv"))
