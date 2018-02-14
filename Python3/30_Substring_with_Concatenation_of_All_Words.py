#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/14
class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []

        word_length = len(words[0])
        words_length = word_length * len(words)
        dic = {}
        for word in words:
            dic[word] = dic[word] + 1 if word in dic else 1

        res = []

        def find(s, l, r, curr):
            if l >= r:
                return True
            word = s[l:l + word_length]
            if word in dic:
                curr[word] = curr[word] + 1 if word in curr else 1
                if curr[word] > dic[word]:
                    return False
                else:
                    return find(s, l + word_length, r, curr)
            else:
                return False

        for i in range(len(s) - words_length + 1):
            if find(s, i, i + words_length, {}):
                res.append(i)
        return res


class Solution2:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words == []:
            return []
        word_length = len(words[0])
        words_length = word_length * len(words)
        if len(s) < words_length:
            return []
        res = []

        def find(s, words):
            if len(words) == 0:
                return True
            if s[:word_length] in words:
                words.remove(s[:word_length])
                return find(s[word_length:], words)
            else:
                return False

        for i in range(len(s) - words_length + 1):
            if find(s[i:i + words_length], words[:]):
                res.append(i)
        return res

if __name__ == '__main__':
    s = "aabbaacbbaacdyangacbabc"
    words = ['aa', 'bb']
    so = Solution()
    res = so.findSubstring(s, words)
    print(res)

