class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length
        left, right = 1, 1
        for i in range(length):
            res[i] *= left
            left *= nums[i]
            res[length - i - 1] *= right
            right *= nums[length - i - 1]
        return res
