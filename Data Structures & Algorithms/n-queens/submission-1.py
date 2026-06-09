class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for i in range(n)]
        res = []

        # Check for if a queen can be placed
        def isValid(r, c):
            for i in range(n):
                if board[i][c] == "Q":
                    return False
            
            nr, nc = r - 1, c - 1
            while nr >= 0 and nc >= 0:
                if board[nr][nc] == "Q":
                    return False
                nr, nc = nr - 1, nc - 1

            nr, nc = r - 1, c + 1
            while nr >= 0 and nc < n:
                if board[nr][nc] == "Q":
                    return False
                nr, nc = nr - 1, nc + 1
            
            return True

        def backtrack(r):
            # End of board
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)
                return
            
            for c in range(n):
                if isValid(r, c):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."
        
        backtrack(0)
        return res

