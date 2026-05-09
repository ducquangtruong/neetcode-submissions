class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Find the indexes of the nearest shorter bars at each index
        # Use a strictly increasing stack to track the INDEX
        n = len(heights)
        leftStack, rightStack = [], []
        leftMax = [-1] * n
        rightMax = [n] * n

        for i in range(n):
            while leftStack and heights[leftStack[-1]] >= heights[i]:
                leftStack.pop()
            
            if leftStack:
                leftMax[i] = leftStack[-1]
            
            leftStack.append(i)

            while rightStack and heights[rightStack[-1]] >= heights[n - 1 - i]:
                rightStack.pop()
            
            if rightStack:
                rightMax[n - 1 - i] = rightStack[-1]
            
            rightStack.append(n - 1 - i)
        
        maxArea = 0
        for i in range(n):
            # Use the current bar as the height
            leftMax[i] += 1
            rightMax[i] -= 1
            currentArea = heights[i] * (rightMax[i] - leftMax[i] + 1)
            maxArea = max(maxArea, currentArea)
        
        return maxArea
