class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        seen = set()
        res = 0
        for num in nums:
            if num in seen:
                continue
            curRes = 0
            while num + curRes in numSet:
                curRes += 1
                seen.add(num + curRes)
            res = max(res, curRes)
        return res
