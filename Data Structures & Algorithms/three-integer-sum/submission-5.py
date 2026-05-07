class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()

        i = 0

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue
            target = -nums[i]
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = nums[j] + nums[k]
                if curr_sum == target:
                    res.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif curr_sum < target:
                    j += 1
                else:        
                    k -= 1
        
        return [list(x) for x in res]