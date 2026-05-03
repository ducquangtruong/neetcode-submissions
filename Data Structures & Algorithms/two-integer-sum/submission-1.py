class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        table = {}
        for i, num in enumerate(nums):
            if num in table:
                return [table[num], i]
            else:
                table[target-num] = i
        
        return [-1, -1]