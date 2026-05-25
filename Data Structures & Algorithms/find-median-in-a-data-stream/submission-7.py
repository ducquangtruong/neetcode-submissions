class MedianFinder:

    def __init__(self):
        # Idea: Keep a maxHeap for smaller half, minHeap for bigger half
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        top = self.left[0] if self.left else float("-inf")
        bottom = self.right[0] if self.right else float("inf")
        # Push and then rebalance the heaps
        if num <= top:
            heapq.heappush_max(self.left, num)
            if len(self.left) - len(self.right) > 1:
                num = heapq.heappop_max(self.left)
                heapq.heappush(self.right, num)
        else:
            heapq.heappush(self.right, num)
            if len(self.right) - len(self.left) > 0:
                num = heapq.heappop(self.right)
                heapq.heappush_max(self.left, num)

    def findMedian(self) -> float:
        total = len(self.left) + len(self.right)
        if total % 2 == 0:
            return (self.left[0] + self.right[0]) / 2
        return self.left[0]
        