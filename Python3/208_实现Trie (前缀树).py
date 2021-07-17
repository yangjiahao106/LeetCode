class Node():
    def __init__(self):
        self.is_end = False
        self.children = dict()


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        n = self.root
        for c in word:
            if c not in n.children:
                n.children[c] = Node()
            n = n.children[c]
        n.is_end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        n = self.root
        for c in word:
            if c in n.children:
                n = n.children[c]
            else:
                return False
        if n.is_end:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        n = self.root
        for c in prefix:
            if c in n.children:
                n = n.children[c]
            else:
                return False
        return True


class Trie2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = dict()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        if not word:
            return None

        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = dict()
            cur = cur[c]

        cur['leaf'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for c in word:
            if c in cur:
                cur = cur[c]
            else:
                return False

        return 'leaf' in cur

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        cur = self.root
        for c in prefix:
            if c in cur:
                cur = cur[c]
            else:
                return False
        return True
