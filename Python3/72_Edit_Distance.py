#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/2
class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        参考：http://blog.csdn.net/feliciafay/article/details/17502919
        时间O(mn)
        空间O(2n)
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        pre = [i for i in range(l2)]

        for i in range(l1):
            cur = [i] * l2
            for j in range(1, l2):
                cur[j] = min(pre[j] + 1, cur[j - 1] + 1, pre[j - 1] + (word1[i - 1] != word2[j - 1]))
            pre = cur[:]

        return pre[-1]



class Solution2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        空间O(n)
        时间O(mn)
        """
        l1, l2 = len(word1) + 1, len(word2) + 1
        dp = list(range(l2))

        for i in range(1, l1):
            pre, dp[0] = i - 1, i
            for j in range(1, l2):
                buf = dp[j]
                dp[j] = min(dp[j] + 1, dp[j - 1] + 1, pre + (word1[i - 1] != word2[j - 1]))
                pre = buf

        return dp[-1]
