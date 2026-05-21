class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapq.heapify_max(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop_max(stones), heapq.heappop_max(stones)
            diff = stone1 - stone2
            if diff:
                heapq.heappush_max(stones, abs(diff))
        
        return stones[-1] if stones else 0