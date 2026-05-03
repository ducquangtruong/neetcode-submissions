class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i, height in enumerate(heights):
            newI = i
            # Strictly increasing stack; the new bar can take the old index to store the left boundary
            while len(stack) > 0 and height <= stack[-1][1]:
                oldI, oldHeight = stack.pop()
                res = max(res, oldHeight * (i - oldI))
                newI = oldI
            stack.append([newI, height])
        
        # The right boundary is now the end of the histogram
        for remain in stack:
            res = max(res, remain[1] * (len(heights) - remain[0]))
        
        return res
