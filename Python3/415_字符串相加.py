class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = list(num1)
        num2 = list(num2)
        res = []
        carry = 0
        while num1 or num2 or carry:
            x = carry
            if num1:
                x += ord(num1.pop()) - ord('0')
            if num2:
                x += ord(num2.pop()) - ord('0')
            carry = x // 10
            res.append(str(x % 10))
        return "".join(res[::-1])
