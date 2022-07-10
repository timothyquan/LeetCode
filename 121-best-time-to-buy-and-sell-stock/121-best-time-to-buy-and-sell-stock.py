class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = float('inf')
        maxprofit = 0
        for val in prices:
            if val < low: low = val
            if val - low > maxprofit: maxprofit = val -low
                
        return maxprofit
            
        