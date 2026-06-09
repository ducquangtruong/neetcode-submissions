class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if not cur.children[idx]:
                cur.children[idx] = TrieNode()
            cur = cur.children[idx]
        
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(cur, target):
            if target == "":
                return cur.endOfWord
            for i in range(len(target)):
                if target[i] != ".":
                    idx = ord(target[i]) - ord("a")
                    if not cur.children[idx]:
                        return False
                    cur = cur.children[idx]
                if target[i] == ".":
                    for child in cur.children:
                        if child and dfs(child, target[i+1:]):
                            return True
                    return False

            return cur.endOfWord
        
        return dfs(self.root, word)
            
