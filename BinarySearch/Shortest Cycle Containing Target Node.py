


class Solution:
    def solve(self, graph, target):
        from collections import deque
        visited = set()
        q = deque()
        q.append(target)
        res = 0
        while q:
            res += 1
            for i in range(len(q)):
                v = q.popleft()
                for next_v in graph[v]:
                    if next_v == target:
                        return res

                    if next_v not in visited:
                        visited.add(next_v)
                        q.append(next_v)

        return -1
