#! python3
# __author__ = "YangJiaHao"
# date: 2021/5/14

class Solution:
    def decodeString(self, s: str) -> str:
        int_stack = []
        stack = []
        i = 0
        while i < len(s):
            if '0' <= s[i] <= '9':
                l = i
                while '0' <= s[i] <= '9':
                    i += 1
                int_stack.append(int(s[l:i]))

            if s[i] == ']':
                tmp = ""
                while True:
                    c = stack.pop()
                    if c == '[':
                        break
                    tmp = c + tmp
                stack.append(tmp * int_stack.pop())
            else:
                stack.append(s[i])

            i += 1

        return "".join(stack)

if __name__ == '__main__':
    print(Solution().decodeString("3[a]2[bc]"))