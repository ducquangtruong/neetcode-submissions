class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap = []
        for num in nums:
            heapq.heappush(self.minHeap, num)
        self.capacity = k

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while len(self.minHeap) > self.capacity:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]