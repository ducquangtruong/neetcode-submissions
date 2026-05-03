class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        length = len(sortedNums)
        res = set()
        ans = []

        for i in range(length - 2):
            searchRes = self.twoSum(i + 1, length - 1, sortedNums, -sortedNums[i])
            for pair in searchRes:
                res.add((sortedNums[i], sortedNums[pair[0]], sortedNums[pair[1]]))
        
        for tup in res:
            ans.append([tup[0], tup[1], tup[2]])
        
        return ans
    
    def twoSum(self, start: int, end: int, nums: List[int], target: int):
        l, r = start, end
        res = []
        while l < r:
            if nums[l] + nums[r] == target:
                res.append([l, r])
                l += 1
                r -= 1
            if nums[l] + nums[r] < target:
                l += 1
            if nums[l] + nums[r] > target:
                r -= 1
        return res