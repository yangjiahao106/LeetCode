#! python3
# __author__ = "YangJiaHao"
# date: 2018/3/17

# 两个stack 实现queue
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            self.stack2 = self.stack1[::-1]
            self.stack1 = []

        return self.stack2.pop()

from queue import Queue


# 两个queue 实现stack
class MyStack(object):
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self,node):
        self.q1.put(node)

    def pop(self):
        if self.q1.empty():
            while not self.q2.empty():
                val = self.q2.get()
                if self.q2.empty():
                    return val
                else:
                    self.q1.put(val)
        else:
            while not self.q1.empty():
                val = self.q1.get()
                if self.q1.empty():
                    return val
                else:
                    self.q2.put(val)


if __name__ == '__main__':
    s = MyStack()
    s.push(1)
    s.push(2)
    print(s.pop())
    s.push(3)
    print(s.pop())
    print(s.pop())

