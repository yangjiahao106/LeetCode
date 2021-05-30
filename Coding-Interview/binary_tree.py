#! python3
# __author__ = "YangJiaHao"
# date: 2017/10/23
from queue import Queue


class Node(object):
    def __init__(self, val=-1, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def add(self, val):
        node = Node(val)
        if self.root is None:
            self.root = node
        else:
            queue_ = Queue()
            queue_.put(self.root)
            while True:
                cur = queue_.get()
                if cur.left is None:
                    cur.left = node
                    return
                elif cur.right is None:
                    cur.right = node
                    return
                else:
                    queue_.put(cur.left)
                    queue_.put(cur.right)

    def pre_order(self, node):
        # 前序遍历 中 -> 左 -> 右
        if not isinstance(node, Node) or not node:
            return
        print(node.val, end=" ")
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        # 中序遍历 左 -> 中 -> 右

        if not isinstance(node, Node) or not node:
            return
        self.in_order(node.left)
        print(node.val, end=" ")
        self.in_order(node.right)

    def post_order(self, node):
        # 后序遍历 左 -> 右 -> 中
        if not isinstance(node, Node) or not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val, end=" ")

    def level_order(self):
        # 水平遍历
        if self.root is None:
            return
        que = Queue()
        que.put(self.root)
        while not que.empty():
            cur = que.get()  # 先进先出
            print(cur.val, end=" ")
            if cur.left:
                que.put(cur.left)
            if cur.right:
                que.put(cur.right)

    def look_up(self):
        # 水平遍历，简洁版本
        row = [self.root]
        while row:
            for node in row:
                print(node.val, end="")
            print('')
            row = [kid for node in row for kid in (node.left, node.right) if kid]

    def max_depth(self, node):
        # 树的最大深度
        if node is None:
            return 0
        return max(self.max_depth(node.left), self.max_depth(node.right)) + 1

    def is_same_tree(self, p, q):
        # 比较两棵树是否一样
        if p is None and q is None:
            return True

        elif p and q:
            return p.val == q.val and self.is_same_tree(p.left, q.left) and self.is_same_tree(p.right, q.right)

        else:
            return False

            # @staticmethod
            # def level_order(root_in):
            #     if root_in is None:
            #         return
            #     q = Queue()
            #     q.put(root_in)
            #
            #     while not q.empty():
            #         cur = q.get()
            #         print(cur.val, end=' ')
            #         if cur.left is not None:
            #             q.put(cur.left)
            #         if cur.right is not None:
            #             q.put(cur.right)


def rebuild_binary_tree(pre, tin):
    if not pre:
        return None

    val = pre[0]

    index = tin.index(val)
    root = Node(val)

    root.left = rebuild_binary_tree(pre[1:index + 1], tin[:index])
    root.right = rebuild_binary_tree(pre[index + 1:], tin[index + 1:])

    return root


def reConstructBinaryTree(pre, tin):
    if not pre:
        return None

    root_val = pre[0]
    index = tin.index(root_val)
    root = Node(root_val)

    root.left = reConstructBinaryTree(pre[1:index + 1], tin[:index])

    root.right = reConstructBinaryTree(pre[index + 1:], tin[index + 1:])

    return root


if __name__ == '__main__':
    tree = BinaryTree()
    vals = [1, 2, 3, 4, 5, 6, 7]
    for v in vals:
        tree.add(v)

    tree.root = rebuild_binary_tree([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3, 7])

    print('pre order:')
    tree.pre_order(tree.root)

    print('\nin order:')
    tree.in_order(tree.root)

    print('\nlevel order:')
    tree.level_order()

    print('\nlevel order one line:')

    tree.look_up()
