class MedianFinder:

    def __init__(self):
        # Idea: Keep a maxHeap for smaller half, minHeap for bigger half
        self.smaller = []
        self.bigger = []

    def addNum(self, num: int) -> None:
        heapq.heappush_max(self.smaller, num)
        if (
            len(self.smaller) - len(self.bigger) > 1 or
            (self.bigger and self.bigger[0] < self.smaller[0])
        ):
            num = heapq.heappop_max(self.smaller)
            heapq.heappush(self.bigger, num)
        if len(self.bigger) - len(self.smaller) > 0:
            num = heapq.heappop(self.bigger)
            heapq.heappush_max(self.smaller, num)

    def findMedian(self) -> float:
        total = len(self.smaller) + len(self.bigger)
        if total % 2 == 0:
            return (self.smaller[0] + self.bigger[0]) / 2
        return self.smaller[0]
        