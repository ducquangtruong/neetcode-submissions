class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        l, r = 0, 1
        res = 0

        while l < r and r < len(prices):
            res = max(res, prices[r] - prices[l])
            while l < r and prices[l] >= prices[r]:
                l += 1
            r += 1
        
        return res