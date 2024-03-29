#! python3
# __author__ = "YangJiaHao"
# date: 2018/1/27
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        :runtime: 1280ms
        """
        length = len(s)
        start = 0
        end = 1
        for center in range(length):
            len1 = self.expand(s, length, center, center)
            if center < length-1 and s[center] == s[center+1]:
                len2 = self.expand(s, length, center, center + 1)
                len1 = max(len1, len2)
            if len1 > end - start:
                start = center - (len1 - 1)//2
                end = center + len1//2 +1

        return s[start:end]

    def expand(self, s, length, left, right):
        while left >= 0 and right < length and s[left] == s[right]:
            left -=1
            right +=1
        return right - left -1


class Solution2:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        :runtime: 95ms
        """
        if len(s) == 0:
            return 0

        max_l = 1
        max_s = s[0]
        for i in range(len(s)):
            check_odd = s[i - max_l - 1:i + 1]
            check_even = s[i - max_l:i + 1]
            if i - max_l >= 1 and check_odd == check_odd[::-1]:
                max_s = check_odd
                max_l += 2
            if i - max_l >= 0 and check_even == check_even[::-1]:
                max_s = check_even
                max_l += 1
        return max_s


if __name__ == '__main__':
    solution = Solution()
    pa = solution.longestPalindrome("abcbcb")
    print(pa)