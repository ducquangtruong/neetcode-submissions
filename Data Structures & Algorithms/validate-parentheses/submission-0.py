class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            match c:
                case ")":
                    if not stack or stack[-1] != "(":
                        return False
                    stack.pop()
                case "]":
                    if not stack or stack[-1] != "[":
                        return False
                    stack.pop()
                case "}":
                    if not stack or stack[-1] != "{":
                        return False
                    stack.pop()
                case _:
                    stack.append(c)
        
        return len(stack) == 0