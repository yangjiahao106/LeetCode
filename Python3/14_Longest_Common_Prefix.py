#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/7

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""
        if len(strs) == 1:
            return strs[0]
        i = 0
        while True:
            prev = None
            for str in strs:
                if len(str) <= i or (prev and prev != str[i]):
                    return str[:i]
                prev = str[i]
            i += 1


class Solution2(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)


if __name__ == '__main__':
    so = Solution()
    ret = so.longestCommonPrefix(['csds', 'c'])
    print(ret)
