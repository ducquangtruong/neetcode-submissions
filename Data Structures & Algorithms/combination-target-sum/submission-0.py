class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        def dfs(i, target):
            if target == 0:
                res.append(sub.copy())
                return
            if i > len(nums) - 1 or target < 0:
                return
            sub.append(nums[i])
            dfs(i, target - nums[i])
            sub.pop()
            dfs(i + 1, target)
        
        dfs(0, target)
        return res