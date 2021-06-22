from typing import *


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+', '-', '*', '/']

        stack = []
        for t in tokens:
            if t in op:
                r = int(stack.pop())
                l = int(stack.pop())
                if t == '+':
                    stack.append(l + r)
                elif t == '-':
                    stack.append(l - r)
                elif t == '*':
                    stack.append(l * r)
                elif t == '/':
                    stack.append(l / r)
            else:
                stack.append(t)

        return int(stack[0])