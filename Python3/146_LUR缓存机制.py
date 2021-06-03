class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next: Node = None
        self.pre: Node = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num = 0
        self.head = Node(0, -1)
        self.tail = None
        self.dict = dict()

    def get(self, key: int) -> int:
        if key in self.dict:
            node: Node = self.dict[key]
            node.pre.next = node.next
            if node.next:
                node.next.pre = node.pre
            elif node.pre != self.head:
                self.tail = node.pre  # 更新tail
            if self.head.next:
                self.head.next.pre = node
            node.next = self.head.next
            self.head.next = node
            node.pre = self.head
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update
        if key in self.dict:
            self.get(key)
            self.dict[key].val = value

        else:
            # 插入
            node = Node(key, value)
            self.dict[key] = node
            node.next = self.head.next
            if self.head.next:
                self.head.next.pre = node
            self.head.next = node
            node.pre = self.head

            if self.tail is None:  # 初始化 Tail
                self.tail = node

                # 删除尾部节点
            if self.num >= self.capacity:
                del self.dict[self.tail.key]
                pre = self.tail.pre
                self.tail.pre.next = None
                self.tail = pre

            else:
                self.num += 1


if __name__ == '__main__':
    # ["LRUCache","put","put","get","put","get","put","get","get","get"]
    # [[2],[1,0],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    c = LRUCache(2)
    print(c.put(2, 1))
    print(c.put(2, 2))
    print(c.get(1))
    print(c.put(1, 1))
    print(c.put(4, 1))
    print(c.get(3))
