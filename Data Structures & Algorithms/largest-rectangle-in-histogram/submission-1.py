class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Idea: For each bar, we store the left and right boundary to calculate the area made using that bar
        n = len(heights)
        stack = []
        res = 0

        for i, h in enumerate(heights):
            start = i
            # Strictly increasing stack; the new bar can take the old index to store the left boundary
            while stack and h <= stack[-1][1]:
                idx, height = stack.pop()
                res = max(res, height * (i - idx))
                start = idx
            stack.append([start, h])

        # The right boundary is now the end of the histogram
        for i, h in stack:
            res = max(res, h * (n - i))
        
        return res
