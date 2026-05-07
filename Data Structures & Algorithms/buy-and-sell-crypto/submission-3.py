class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start, end = 0, 0
        res = 0
        while end < len(prices):
            if prices[end] <= prices[start]:
                start = end
            res = max(res, prices[end] - prices[start])
            end += 1
        
        return res