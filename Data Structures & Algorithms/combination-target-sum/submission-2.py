class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        cur = []

        def dfs(remain, i):
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0 or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(remain - nums[i], i)
            cur.pop()
            dfs(remain, i + 1)
        
        dfs(target, 0)
        return res