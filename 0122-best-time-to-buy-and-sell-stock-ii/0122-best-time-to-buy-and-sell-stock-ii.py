class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        total_profit = 0
        buy = 10001
        
        for price in prices:
            if buy > price:
                buy = price
            else:
                profit = price - buy
                total_profit = total_profit + profit
                buy = price
        
        return total_profit