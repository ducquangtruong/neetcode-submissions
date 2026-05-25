class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        pick = [False] * len(nums)
        cur = []

        def backtrack():
            if len(cur) == len(nums):
                res.append(cur[:])
                return
            
            for i in range(len(nums)):
                if not pick[i]:
                    cur.append(nums[i])
                    pick[i] = True
                    backtrack()
                    cur.pop()
                    pick[i] = False
            
        backtrack()
        return res

