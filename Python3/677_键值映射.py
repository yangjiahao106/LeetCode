class MapSum:
    """
    前缀树变种

    """

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {'sum': 0}

    def insert(self, key: str, val: int) -> None:
        old_val = self.search(key)
        diff = val - old_val
        cur = self.root
        for c in key:
            if c in cur:
                cur = cur[c]
                cur['sum'] += diff
            else:
                cur[c] = {'sum': val}
                cur = cur[c]

        cur['val'] = val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return 0

        return cur['sum']

    def search(self, key: str) -> int:
        cur = self.root
        for c in key:
            if c in cur:
                cur = cur[c]
            else:
                return 0
        if 'val' in cur:
            return cur['val']
        return 0
