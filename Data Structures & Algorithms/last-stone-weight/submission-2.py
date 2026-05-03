class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:
            stoneA = heapq.heappop(heap)
            stoneB = heapq.heappop(heap)
            if stoneA < stoneB:
                heapq.heappush(heap, stoneA - stoneB)
        heap.append(0)
        return abs(heap[0])