class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = 10001
        
        for price in prices:
            if buy > price:
                buy = price
            else:
                sell_profit = price - buy
                if sell_profit > profit:
                    profit = sell_profit
        
        return profit
            
            