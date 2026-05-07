class Solution:
    def isValid(self, s: str) -> bool:
        stk = []
        table = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for chr in s:
            if chr not in table:
                stk.append(chr)
            else:
                if len(stk) == 0 or stk.pop() != table[chr]:
                    return False
        
        return len(stk) == 0