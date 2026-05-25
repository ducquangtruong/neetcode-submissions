class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort so we can skip indexes (no repeats)
        nums.sort()
        res = []
        cur = []

        def dfs(remain, i):
            if remain == 0:
                res.append(cur.copy())
                return
            if remain < 0 or i == len(nums):
                return
            
            cur.append(nums[i])
            dfs(remain - nums[i], i + 1)
            cur.pop()
            # Jump to the next unique number
            i = i + 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(remain, i)
        
        dfs(target, 0)
        return res