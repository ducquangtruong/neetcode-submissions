class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Treat the 2D matrix as a long 1D array
        rows, cols = len(matrix), len(matrix[0])
        l, r = 0, rows * cols - 1
        while l <= r:
            m = (l + r) // 2
            i = m // cols
            j = m % cols

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                r = m - 1
            else:
                l = m + 1
        
        return False