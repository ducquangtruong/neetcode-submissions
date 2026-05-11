class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        def calculateEatingTime(h):
            res = 0
            for pile in piles:
                res += math.ceil(pile / h)
            return res
        
        # Binary search on the rate of banana eating
        l, r = 1, max(piles)
        res = 1
        # for i in range(l, r+1):
            # print(i, calculateEatingTime(i))
        while l <= r:
            m = (l + r) // 2
            # print(l, m, r)
            time = calculateEatingTime(m)
            if time <= h:
                r = m - 1
                res = m
            else:
                l = m + 1
        
        return res