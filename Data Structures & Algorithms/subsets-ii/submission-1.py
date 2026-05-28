class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        cur = []
        
        def dfs(i):
            if i == len(nums):
                res.append(cur[:])
                return
            
            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            i = i + 1
            while i < len(nums) and nums[i] == nums[i-1]:
                i += 1
            dfs(i)
        
        dfs(0)
        return res