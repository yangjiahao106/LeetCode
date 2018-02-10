#! python3
# __author__ = "YangJiaHao"
# date: 2018/1/28
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if length <= 2 or numRows == 1:
            return s
        strs = []
        lag = 2 * (numRows - 1)
        for i in range(numRows):
            j = 0
            while (i + lag * j) < length:
                strs.append(s[i + lag * j])
                if i > 0 and i < numRows - 1:
                    step = i + lag * j + (lag - 2 * i)
                    if step < length:
                        strs.append(s[step])
                j += 1
        return "".join(strs)

    def convert2(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        index, step = 0, 1

        for x in s:
            L[index] += x
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        return ''.join(L)

if __name__ == '__main__':
    # P   A   H   N
    # A P L S I I G
    # Y   I   R
    s = "PAYPALISHIRING"

    solution = Solution()
    s = solution.convert("0123456789", 4)
    print(s)
