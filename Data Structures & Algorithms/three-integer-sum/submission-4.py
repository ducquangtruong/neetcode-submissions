class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        for i in range(len(nums)):
            target = -nums[i]
            start, end = i + 1, len(nums) - 1
            while start < end:
                curr_sum = nums[start] + nums[end]
                if curr_sum == target:
                    res.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif curr_sum < target:
                    start += 1
                else:        
                    end -= 1
        
        return [list(x) for x in res]