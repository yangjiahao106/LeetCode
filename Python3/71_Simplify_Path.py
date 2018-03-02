#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/2
class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        path = path.split('/')
        result = []
        for each in path:
            if each == '.':
                pass
            elif each == '..':
                if result:
                    result.pop()
            elif each != '':
                result.append(each)

        return '/' + '/'.join(result)


if __name__ == '__main__':
    so = Solution()
    res = so.simplifyPath('"/a/./b///../c/../././../d/../../../e/./f/./g/././//.//h///././/..///"')
    print(res)
