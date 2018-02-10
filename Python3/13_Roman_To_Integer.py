#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/6
import re


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        res = re.match("(M*)(CM|[CD]*)?(XC|[XL]*)?(IX|[IV]*)?", s)
        nums = res.groups()
        th = M.index(nums[0])
        hu = C.index(nums[1])
        te = X.index(nums[2])
        si = I.index(nums[3])
        num = si + te * 10 + hu * 100 + th * 1000
        return num

class Solution2:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        last = None
        sum = 0
        s = s[::-1]
        for elem in s:
            if last and dict[last]>dict[elem]:
                sum -= 2*dict[elem]
            sum += dict[elem]
            last = elem
        return sum

if __name__ == '__main__':
    s = Solution2()
    r = s.romanToInt("IX")
    print(r)
