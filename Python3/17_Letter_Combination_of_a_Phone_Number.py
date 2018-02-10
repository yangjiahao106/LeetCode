#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/8
class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) <= 0:
            return []
        keys = [[''], [''], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'],
                ['m', 'n', 'o'], ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]

        result = [""]
        for i in digits:
            temp = []
            for one in result:
                for w in keys[int(i)]:
                    temp.append(one + w)
            result = temp

        return result


class Solution2:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if len(digits) == 0:
            return result
        result = ['']
        string = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                  ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        for c in digits:

            tmp = []
            for c1 in result:
                for c2 in string[int(c)]:
                    tmp.append(c1 + c2)
            result = tmp
        return result

if __name__ == '__main__':
    so = Solution2()
    ret = so.letterCombinations("234")
    print(ret)
