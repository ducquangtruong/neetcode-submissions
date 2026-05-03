class Solution:
    def findMin(self, nums: List[int]) -> int:
        start, end = 0, len(nums) - 1
        if nums[start] < nums[end]:
            return nums[start]

        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start] and nums[mid] > nums[end]:
                start = mid
            else:
                end = mid
            print(start, end)

        return nums[(start + 1) % len(nums)]