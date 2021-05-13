#! python3
# __author__ = "YangJiaHao"
# date: 2021/3/22
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution116:
    def connect(self, root: Node) -> Node:
        if root is None or root.left is None:
            return root

        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root


# 117

class Solution117:
    def connect(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        if root.left and root.right:
            root.left.next = root.right
        elif root.left:
            root.left.next = self.getNext(root.next)
        if root.right:
            root.right.next = self.getNext(root.next)
        # 注意这里先右边再左边
        self.connect(root.right)
        self.connect(root.left)
        return root

    """
        // 先连接右边，下边的递归函数getNext才有效
        // 先确保 root.right 下的节点的已完全连接，因 root.left 下的节点的连接需要 root.left.next 下的节点的信息，若 root.right 下的节点未完全连
        // 接（即先对 root.left 递归），则 root.left.next 下的信息链不完整，将返回错误的信息。可能出现的错误情况如下图所示。
        // 此时，底层最左边节点将无法获得正确的 next 信息：
        //                  o root
        //                 / \
        //     root.left  o —— o  root.right
        //               /    / \
        //              o —— o   o
        //             /        / \
        //            o        o   o
    """

    def getNext(self, root):
        if root is None:
            return root
        if root.left:
            return root.left
        if root.right:
            return root.right
        if root.next:
            return self.getNext(root.next)

    # 非递归版本
    def solution2(self, root: Node):
        if root is None:
            return root
        most_left = root.left
        cur = root
        while cur:
            if most_left is None:
                if cur.left:
                    most_left = cur.left
                elif cur.right:
                    most_left = cur.right
            next = cur.next
            while next:
                if next.left or next.right:
                    break
                next = next.next

            if cur.left and cur.right:
                cur.left.next = cur.right

            if next:
                if next.left:
                    n = next.left
                else:
                    n = next.right
                if cur.left and cur.right is None:
                    cur.left = n
                if cur.right:
                    cur.right.next = n

            if next:
                cur = next
            else:
                cur = most_left
                most_left = None
        return root

    # 网上版本
    def solution3(self, root: 'Node') -> 'Node':
        dummy_left_node = Node()
        pre = dummy_left_node
        current_node = root

        while current_node:
            if current_node.left:
                pre.next = current_node.left
                pre = pre.next
            if current_node.right:
                pre.next = current_node.right
                pre = pre.next

            current_node = current_node.next

            if not current_node:
                current_node = dummy_left_node.next
                dummy_left_node.next = None
                pre = dummy_left_node
        return root

class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.vals = []

    def push(self, x: int) -> None:
        if len(self.vals) < self.maxSize:
            self.vals.append(x)

    def pop(self) -> int:
        if len(self.vals) == 0:
            return -1
        return self.vals.pop(x)

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k,len(self.vals))):
            self.vals[i] += val


