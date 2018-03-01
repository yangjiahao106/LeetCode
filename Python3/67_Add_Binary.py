#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = [int(x) for x in reversed(a)]  # 反转字符串，并转换成list
        b = [int(x) for x in reversed(b)]
        if len(a) > len(b):  # 在短的后面补充0，使长度相同
            b += [0] * (len(a) - len(b))
        elif len(a) < len(b):
            a += [0] * (len(b) - len(a))

        res, carry = [], 0

        for i in range(len(b)):
            if a[i] + b[i] + carry <= 1:
                res.append(a[i] + b[i] + carry)
                carry = 0
            else:
                res.append(a[i] + b[i] + carry - 2)
                carry = 1

        if carry == 1:
            res.append(1)
        res.reverse()
        res = [str(x) for x in res]
        return ''.join(res)


if __name__ == '__main__':
    so = Solution()
    res = so.addBinary('01', '111')
    print(res)
