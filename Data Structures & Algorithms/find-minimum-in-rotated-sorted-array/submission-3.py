class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l + r) // 2
            # If right half is sorted, the min is not there
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        
        return nums[l]
