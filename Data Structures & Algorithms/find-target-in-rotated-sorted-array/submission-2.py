class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find the minimum of array first
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l+r)//2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        pivot = l
        if target > nums[-1]:
            l, r = 0, pivot - 1 if pivot > 0 else len(nums) - 1
        else:
            l, r = pivot, len(nums) - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return -1