import random


class Node:
    def __init__(self, val=0):
        self.val = val
        self.right = None
        self.down = None


class Skiplist:

    def __init__(self):
        left_nodes = [Node(-1) for i in range(16)]
        for i in range(15):
            left_nodes[i].down = left_nodes[i + 1]

        self.lefts = left_nodes

    def search(self, target: int) -> bool:
        cur = self.lefts[0]
        while cur:
            if cur.right and cur.right.val == target:
                return True
            elif cur.right and cur.right.val < target:
                cur = cur.right
            else:
                cur = cur.down
        return False

    def add(self, num: int) -> None:
        cur = self.lefts[0]
        stack = []
        while cur:
            if cur.right and cur.right.val <= num:
                cur = cur.right
            else:
                stack.append(cur)
                cur = cur.down

        pre = None

        while stack:
            cur = stack.pop()
            newNode = Node(num)
            newNode.right = cur.right
            cur.right = newNode
            newNode.down = pre
            pre = newNode
            if random.randint(0, 1):
                break

    def erase(self, num: int) -> bool:
        cur = self.lefts[0]
        find = False
        while cur:
            if cur.right and cur.right.val == num:
                cur.right = cur.right.right
                cur = cur.down
                find = True
            elif cur.right and cur.right.val < num:
                cur = cur.right
            else:
                cur = cur.down
        return find


if __name__ == '__main__':
    s = Skiplist()
    s.add(1)
    s.add(2)
    s.add(3)
    print(s.search(1))