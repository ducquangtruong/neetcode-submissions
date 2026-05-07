class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stk = []
        for i, temp in enumerate(temperatures):
            while stk and stk[-1][0] < temp:
                res[stk[-1][1]] = i - stk[-1][1]
                stk.pop()
            
            stk.append((temp, i))
            
        return res