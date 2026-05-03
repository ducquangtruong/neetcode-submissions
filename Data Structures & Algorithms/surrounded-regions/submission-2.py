class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        visit = set()

        safe = set()
        q = deque()

        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
            if board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
        for c in range(COLS):
            if board[0][c] == "O":
                q.append((0, c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
        
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                visit.add((r, c))
                safe.add((r, c))
                for dr, dc in dirs:
                    row, col = r + dr, c + dc
                    if (
                        min(row, col) >= 0 and row < ROWS and col < COLS
                        and (row, col) not in visit
                        and board[row][col] == "O"
                    ):
                        q.append((row, col))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in safe:
                    board[r][c] = "X"
