class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if (endWord not in wordList) or (beginWord == endWord):
            return 0

        ALPHABET = [chr(c) for c in range(97, 123)]
        words, res = set(wordList), 0
        q = deque([beginWord])

        while q:
            res += 1
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                for i in range(len(word)):
                    for c in ALPHABET:
                        if c == word[i]:
                            continue
                        nei = word[:i] + c + word[i + 1:]
                        if nei in words:
                            q.append(nei)
                            words.remove(nei)

        return 0


    
    def isAdjacent(self, word1, word2):
        diff, n = 0, len(word1)
        for i in range(n):
            if word1[i] != word2[i]:
                diff += 1
        
        return diff == 1
