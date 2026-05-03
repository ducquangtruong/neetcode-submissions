class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        width, height = len(matrix[0]), len(matrix)
        start, end = 0, width * height - 1

        while start <= end:
            mid = (start + end) // 2
            r, c = mid // width, mid % width
            if matrix[r][c] == target:
                return True
            if matrix[r][c] < target:
                start = mid + 1
            if matrix[r][c] > target:
                end = mid - 1

        return False