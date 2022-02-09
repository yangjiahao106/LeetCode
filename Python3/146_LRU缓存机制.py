class Node:
    def __init__(self, k: int, v: int):
        self.key = k
        self.val = v
        self.next = None
        self.pre = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.dict = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.len = 0

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            pre = node.pre
            pre.next = node.next
            node.next.pre = pre
            node.next = self.head.next
            self.head.next.pre = node
            node.pre = self.head
            self.head.next = node

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.get(key)  # move to head
            self.dict[key].val = value

        else:
            node = Node(key, value)
            self.dict[key] = node

            self.head.next.pre = node

            node.next = self.head.next
            self.head.next = node
            node.pre = self.head

            if self.len >= self.cap:
                del self.dict[self.tail.pre.key]
                pre = self.tail.pre
                pre.next = None
                self.tail = pre
            else:
                self.len += 1


class Node():
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.d = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cap = capacity
        self.len = 0

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1
        node = self.d[key]
        self.remove(node)
        self.add_to_head(node)
        return node.v

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.prev = None
        node.next = None

    def add_to_head(self, node):
        next = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = next
        next.prev = node

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            node.v = value
            self.remove(node)
            self.add_to_head(node)
            return

        node = Node(key, value)
        self.d[key] = node
        self.add_to_head(node)

        if self.len == self.cap:
            del self.d[self.tail.prev.k]
            self.remove(self.tail.prev)

        else:
            self.len += 1


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
