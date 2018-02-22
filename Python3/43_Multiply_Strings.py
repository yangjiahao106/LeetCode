#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/21
class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        num1 = [int(x) for x in num1[::-1]]
        num2 = [int(x) for x in num2[::-1]]
        levels = []  #
        for i in num2:
            carry, level = 0, []
            for j in num1:
                remain = (i * j + carry) % 10  # 余数
                carry = (i * j+carry) // 10  # 进位
                level.append(remain)
            level.append(carry)  # 保存最后一次进位
            levels.append(level)

        print(levels)
        result, carry = [], 0

        for i in range(len(levels) + len(levels[0]) - 1):
            s = 0
            for j in range(len(levels)):
                if i - j >= 0 and i - j < len(levels[0]):
                    s += levels[j][i - j]
            result.append((s + carry) % 10)
            carry = (s+carry) // 10

        result.reverse()
        result = [str(x) for x in result]
        result = ''.join(result)
        return result.lstrip('0')


def multiply(num1, num2):
    product = [0] * (len(num1) + len(num2))
    pos = len(product) - 1

    for n1 in reversed(num1):
        tempPos = pos
        for n2 in reversed(num2):
            product[tempPos] += int(n1) * int(n2)
            product[tempPos - 1] += product[tempPos] / 10
            product[tempPos] %= 10
            tempPos -= 1
        pos -= 1

    pt = 0
    while pt < len(product) - 1 and product[pt] == 0:
        pt += 1
    return ''.join(map(str, product[pt:]) or [0])

if __name__ == '__main__':
    so = Solution()
    res = so.multiply("78", "78")
    print(res)
