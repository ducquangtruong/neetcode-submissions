class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stoneA = heapq.heappop(heap)
            stoneB = heapq.heappop(heap)
            heapq.heappush(heap, -abs(stoneA - stoneB))
        return -heap[0]