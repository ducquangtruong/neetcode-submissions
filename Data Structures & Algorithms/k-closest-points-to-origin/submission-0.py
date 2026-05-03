class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hq = []
        for point in points:
            heapq.heappush(hq, [-self.calcDist(point), point])
            if len(hq) > k:
                heapq.heappop(hq)
        return [val[1] for val in hq]
    
    def calcDist(self, point: List[int]) -> float:
        return math.sqrt(point[0] * point[0] + point[1] * point[1])