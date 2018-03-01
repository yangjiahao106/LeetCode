#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        for i, v in enumerate(digits):
            if v < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
                if i == len(digits) - 1:
                    digits.append(1)
                    break
        digits.reverse()
        return digits

class Solution2:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        for i, v in enumerate(digits):
            if v < 9:
                digits[i] += 1
                digits[:i] = [0] * i
                break
            elif i == len(digits) - 1:
                digits.append(1)
                digits[:i + 1] = [0] * (i + 1)
                break
        digits.reverse()
        return digits


if __name__ == '__main__':
    so = Solution()
    res = so.plusOne([9,9])
    print(res)
