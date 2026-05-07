import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        start, end = 0, 0
        res = []

        while end <= len(nums):
            if end - start == k:
                while window[0][1] < start:
                    heapq.heappop_max(window)
                res.append(window[0][0])
                start += 1
            if end < len(nums):
                heapq.heappush_max(window, [nums[end], end])
            end += 1
        
        return res
