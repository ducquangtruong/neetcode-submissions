class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(secondNum + firstNum)
                case "-":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(secondNum - firstNum)
                case "*":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(secondNum * firstNum)
                case "/":
                    firstNum = stack.pop()
                    secondNum = stack.pop()
                    stack.append(math.trunc(secondNum / firstNum))
                case _:
                    stack.append(int(token))
        
        return stack[-1]