class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calculateDist(point):
            return math.sqrt(point[0] ** 2 + point[1] ** 2)

        maxHeap = []
        for point in points:
            heapq.heappush_max(maxHeap, [calculateDist(point), point])
            if len(maxHeap) > k:
                heapq.heappop_max(maxHeap)

        return [x[1] for x in maxHeap]