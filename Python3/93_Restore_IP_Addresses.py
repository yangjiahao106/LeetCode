#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/13
class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        result = []
        self.dfs('', 0, s, result)
        return result

    def dfs(self, one, count, rest, result):
        if count == 4:
            if not rest:
                result.append(one[:-1])
            return

        for i in range(1,4):
            if i <= len(rest):
                if int(rest[:i]) <= 255:
                    self.dfs(one+ rest[:i] + '.',count + 1, rest[i:],result)
                if rest[0] == '0': # 每个ip字段 不能以0开头。但可以为0
                    break


if __name__ == '__main__':
    so = Solution()
    res = so.restoreIpAddresses('010010')
    print(res)
