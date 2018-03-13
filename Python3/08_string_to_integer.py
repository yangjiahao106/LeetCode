#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/3
class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0
        num = ''
        symbol = 1
        if str[0] == '-':
            symbol = -1
            str = str[1:]
        elif str[0] == '+':
            symbol = 1
            str = str[1:]

        for i in str:
            if i < '0' or i > '9':
                break
            else:
                num += i
        if num == "":
            return 0
        num = int(num) * symbol
        if num > 2147483647:
            num = 2147483647
        elif num < -2147483648:
            num = -2147483648
        return num


if __name__ == '__main__':
    so = Solution()
    i = so.myAtoi("+-45")
    print(i)
