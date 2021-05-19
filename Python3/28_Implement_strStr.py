#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/12
class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)

class Solution2:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:
                return i
        return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # sunday 算法
        if len(needle) == 0:
            return 0

        move = dict()
        for i in range(len(needle)):
            move[needle[i]] = i

        i = 0
        while i <= len(haystack) - len(needle): # 注意 当len(haystack)==len(needle)时 这里需要 ==
            j = 0
            while haystack[i + j] == needle[j]:
                j += 1
                if j >= len(needle):
                    return i

            if i < len(haystack) - len(needle) and haystack[i + len(needle)] in move: # 注意当len(haystack) == len(needle) 时可能越界
                i += len(needle) - move[haystack[i + len(needle)]]
            else:
                i += len(needle) + 1

        return -1


if __name__ == '__main__':
    so = Solution()
    res = so.strStr("good", "o")
    print(res)