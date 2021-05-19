#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/1
class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        words.reverse()  # 方便pop
        res = []
        while True:
            line, width = [], 0
            while words:
                if width + len(words[-1]) <= maxWidth - (len(line)):  # 单词之间至少一个空格
                    width += len(words[-1])
                    line.append(words.pop())
                else:
                    break

            ave_space = (maxWidth - width) // ((len(line) - 1) or 1)
            spare_space = (maxWidth - width) % ((len(line) - 1) or 1)
            temp = ''
            for word in line:
                if not temp:  # 放置第一个单词
                    temp = word
                elif not words:  # 最后一行靠左
                    temp = temp + ' ' + word
                elif spare_space > 0:  # 有多余的空格
                    temp = temp + ' ' * (ave_space + 1) + word
                    spare_space -= 1
                else:
                    temp = temp + ' ' * ave_space + word

            if len(line) == 1:
                temp += ' ' * ave_space
            res.append(temp)
            if not words:
                res[-1] = res[-1] + ' ' * (maxWidth - len(res[-1]))  # 最后一行靠左，后面需要补上空格
                return res


class Solution2:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        网友答案，更简介
        """
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                if len(cur) == 1:
                    res.append(cur[0] + ' ' * (maxWidth - num_of_letters))
                else:
                    num_spaces = maxWidth - num_of_letters
                    space_between_words, num_extra_spaces = divmod(num_spaces, len(cur) - 1)
                    for i in range(num_extra_spaces):
                        cur[i] += ' '
                    res.append((' ' * space_between_words).join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        res.append(' '.join(cur) + ' ' * (maxWidth - num_of_letters - len(cur) + 1))
        return res


if __name__ == '__main__':
    so = Solution()
    res = so.fullJustify(["What", "must", "be", "shall", "be."], 12)
    print(res)
