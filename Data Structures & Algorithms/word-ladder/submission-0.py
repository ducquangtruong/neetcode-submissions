class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # Make a graph, then check for a path?
        graph = defaultdict(list)
        for word in wordList:
            length = len(word)
            for i in range(length):
                par = "".join([word[j] if j != i else "*" for j in range(length)])
                graph[par].append(word)

        visit = set()
        q = deque()
        q.append(beginWord)
        res = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                length = len(word)
                pars = [[word[j] if j != i else "*" for j in range(length)] for i in range(length)]
                for par in pars:
                    for nei in graph["".join(par)]:
                        if nei == endWord:
                            return res + 1
                        if nei not in visit:
                            visit.add(nei)
                            q.append(nei)
            res += 1

        return 0


    
    def isAdjacent(self, word1, word2):
        diff, n = 0, len(word1)
        for i in range(n):
            if word1[i] != word2[i]:
                diff += 1
        
        return diff == 1
