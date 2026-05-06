class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        nums_set = set(nums)
        for num in nums:
            # Check if num is the start of sequence
            if num - 1 in nums_set:
                continue
            
            curr_length = 0
            while num in nums_set:
                curr_length += 1
                num += 1
            max_length = max(max_length, curr_length)
        
        return max_length