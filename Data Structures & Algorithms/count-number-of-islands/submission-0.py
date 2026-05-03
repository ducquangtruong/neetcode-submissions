class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = [[False] * COLS for i in range(ROWS)]
        res = 0

        def explore(r, c):
            if (
                r < 0 or c < 0
                or r >= ROWS or c >= COLS
                or visit[r][c] or grid[r][c] != "1"
            ):
                return
            visit[r][c] = True
            explore(r - 1, c)
            explore(r + 1, c)
            explore(r, c - 1)
            explore(r, c + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and not visit[r][c]:
                    explore(r, c)
                    res += 1
        
        return res
