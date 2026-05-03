class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        output = []
        def backtrack(numOfOpening, numOfClosing):
            if len(stack) == n * 2:
                output.append("".join(stack))
                return
            if numOfOpening < n:
                stack.append("(")
                backtrack(numOfOpening + 1, numOfClosing)
                stack.pop()
            if numOfClosing < numOfOpening:
                stack.append(")")
                backtrack(numOfOpening, numOfClosing + 1)
                stack.pop()
        
        backtrack(0, 0)
        
        return output
