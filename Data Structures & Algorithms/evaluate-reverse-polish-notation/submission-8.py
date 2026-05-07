class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stk.append(int(token))
                continue

            num2 = stk.pop()
            num1 = stk.pop()
            match token:
                case "+":
                    stk.append(num1 + num2)
                case "-":
                    stk.append(num1 - num2)
                case "*":
                    stk.append(num1 * num2)
                case "/":
                    stk.append(int(num1 / num2))
                case _:
                    continue
        
        return stk[-1]