class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calTime(speed):
            return sum([math.ceil(pile/speed) for pile in piles])

        start, end = 1, max(piles)
        res = end

        while start <= end:
            mid = (start + end) // 2
            totalTime = calTime(mid)
            if totalTime <= h:
                res = mid
                end = mid - 1
            else:
                start = mid + 1

        return res