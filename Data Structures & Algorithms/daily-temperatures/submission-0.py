class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        for idx, val in enumerate(temperatures):
            while len(stack) > 0 and val > stack[-1][1]:
                oldIdx, oldVal = stack.pop()
                res[oldIdx] = idx - oldIdx
            stack.append([idx, val])
        
        return res