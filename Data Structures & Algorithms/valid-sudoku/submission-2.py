class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row = [board[i][j] if board[i][j] != "." else (i, j) for j in range(9)]
            col = [board[j][i] if board[j][i] != "." else (i, j) for j in range(9)]
            if len(row) != len(set(row)) or len(col) != len(set(col)):
                return False
        
        for i in [1, 4, 7]:
            for j in [1, 4, 7]:
                square = [board[i - di][j - dj] if board[i-di][j-dj] != "." else (i-di, j-dj) for di in [-1, 0, 1] for dj in [-1, 0, 1]]
                if len(square) != len(set(square)):
                    return False
        
        return True