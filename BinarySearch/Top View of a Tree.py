# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# 二叉树顶视图

class Solution:
    def solve(self, root):
        from collections import deque
        index_que = deque()
        index_que.append(0)
        res_que = deque()
        res_que.append(root.val)
        que = deque()
        que.append((root, 0))

        while que:
            node, idx = que.popleft()
            if idx < index_que[0]:
                index_que.appendleft(idx)
                res_que.appendleft(node.val)

            if idx > index_que[-1]:
                index_que.append(idx)
                res_que.append(node.val)

            if node.left:
                que.append((node.left, idx - 1))
            if node.right:
                que.append((node.right, idx + 1))

        return list(res_que)


class Solution2:
    def solve(self, root):
        from collections import deque
        que = deque()
        visited = dict()

        que.append((root, 0))

        while que:
            node, idx = que.popleft()
            if idx not in visited:
                visited[idx] = node.val
            if node.left:
                que.append((node.left, idx - 1))
            if node.right:
                que.append((node.right, idx + 1))

        res = []
        # 使用idx 排序
        for idx in sorted(visited.keys()):
            res.append(visited[idx])
        return res
