class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sub = []

        def dfs(i, target):
            if target == 0:
                res.append(sub.copy())
                return
            if i > len(candidates) - 1 or target < 0:
                return
            sub.append(candidates[i])
            dfs(i + 1, target - candidates[i])
            candidate = sub.pop()
            while i <= len(candidates) - 1 and candidate == candidates[i]:
                i += 1
            dfs(i, target)
        
        dfs(0, target)
        return res