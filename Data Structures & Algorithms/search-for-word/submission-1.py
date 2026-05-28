class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visit = [[False for i in range(cols)] for j in range(rows)]

        def dfs(r, c, idx):
            if idx == len(word):
                return True
            
            if (
                r < 0 or r >= rows or
                c < 0 or c >= cols or
                visit[r][c] or board[r][c] != word[idx]
            ):
                return False
            
            visit[r][c] = True
            res = (
                dfs(r - 1, c, idx + 1) or
                dfs(r + 1, c, idx + 1) or
                dfs(r, c - 1, idx + 1) or
                dfs(r, c + 1, idx + 1)
            )
            visit[r][c] = False
            return res
        
        for i in range(rows):
            for j in range(cols):
                res = dfs(i, j, 0)
                if res:
                    return True
        
        return False