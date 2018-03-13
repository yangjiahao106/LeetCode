#! python3
# __author__ = "YangJiaHao"
# date: 2018/1/26

class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = {}
        start = 0
        end = 0
        theMax = 0
        count = 0
        while end< len(s):
            if arr.get(s[end]) ==1:
                del arr[s[start]]
                start += 1
                count -= 1
            else:
                arr[s[end]] = 1
                end += 1
                count += 1
                theMax = max(count,theMax)
        return theMax

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