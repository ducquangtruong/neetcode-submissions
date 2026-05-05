class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Cumulative product
        left, right = 1, 1
        
        for i in range(len(nums)):
            res[i] *= left
            res[-i-1] *= right
            left *= nums[i]
            right *= nums[-i-1]
        
        return res