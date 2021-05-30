#! python3
# __author__ = "YangJiaHao"
# date: 2018/1/26

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] not in d:
                d[s[r]] = None
                r += 1
                res = max(res, r - l)
            else:
                del d[s[l]]
                l += 1
        return res


class Solution2:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup = {}
        offset = -1
        longest = 0
        for idx, char in enumerate(s):
            if char in lookup:
                if offset < lookup[char]:
                    offset = lookup[char]
            lookup[char] = idx
            length = idx - offset
            if length > longest:
                longest = length
        return longest


if __name__ == '__main__':
    solution = Solution()
    theMax = solution.lengthOfLongestSubstring("aaaabc")
    print(theMax)
