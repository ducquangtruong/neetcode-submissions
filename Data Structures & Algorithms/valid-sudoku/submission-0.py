class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        midSquares = [[1, 1], [4, 1], [7, 1], [1, 4], [4, 4], [7, 4], [1, 7], [4, 7], [7, 7]]

        for i in range(9):
            if not self.check([board[i][j] for j in range(9)]):
                return False
            if not self.check([board[j][i] for j in range(9)]):
                return False
            if not self.check([board[midSquares[i][0] + dx][midSquares[i][1] + dy] for dx in [-1, 0, 1] for dy in [-1, 0, 1]]):
                return False

        return True
    
    # Check duplication for nine squares
    def check(self, squares: List[str]) -> bool:
        seen = set()
        for square in squares:
            if square == ".":
                continue
            if square in seen:
                return False
            seen.add(square)
        return True