#! python3
# __author__ = "YangJiaHao"
# date: 2018/2/3
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        e = len(str(x))

        if e % 2 == 1:
            cut = (e - 1) // 2
        else:
            cut = e // 2
        a = x % (10 ** cut)
        b = x // (10 ** (e - cut))
        c = 0
        print(a, b)
        while b > 0:
            c = 10 * c + b % 10
            b = b // 10
        return a == c

    def isPalindrome2(self, x):
        if x < 0:
            return False
        e = len(str(x))
        for i in range(e//2):
            if x%10 != x//10**(e-1-i*2):
                return False
            x = x//10
            x = x%(10**(e-2-i*2))
        return True

if __name__ == '__main__':
    s = Solution()
    i = s.isPalindrome2(123321)
    print(i)
    #12321