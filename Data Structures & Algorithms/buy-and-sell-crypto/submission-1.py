class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curMin = prices[0]
        profit = 0
        for i in prices:
            
            profit = max(profit, i - curMin)
            curMin = min(curMin, i)
        
        return profit