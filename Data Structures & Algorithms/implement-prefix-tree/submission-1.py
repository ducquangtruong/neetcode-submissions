class TrieNode:
    def __init__(self):
        # Only 26 letters but could use a hashmap for more
        self.children = [None] * 26
        self.endOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]

        cur.endOfWord = True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            idx = ord(c) - ord("a")
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]

        return cur.endOfWord

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not cur.children[idx]:
                return False
            cur = cur.children[idx]

        return True
        