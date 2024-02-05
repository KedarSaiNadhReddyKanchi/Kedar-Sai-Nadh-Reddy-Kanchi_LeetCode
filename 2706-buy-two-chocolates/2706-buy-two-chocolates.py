class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        
        # the solution for this problem is to find the two least values in the array
        # after finding them, get their sum value and check if that sum value is less than or equal to the money
        # if it is then return the difference b/w the sum and money
        # if it is not then return the money value
        
        
        leastPrice1 = 100
        leastPrice2 = 100
        
        for price in prices:
            if leastPrice1 == 100 and leastPrice2 == 100:
                leastPrice1 = price
            elif price < leastPrice1:
                leastPrice2 = leastPrice1
                leastPrice1 = price
            elif price < leastPrice2:
                leastPrice2 = price
        
        total_price_sum = leastPrice1 + leastPrice2
        print(f"leastPrice1 = {leastPrice1} and leastPrice2 = {leastPrice2}, sum = {total_price_sum}")
        
        if (money >= total_price_sum):
            return (money - total_price_sum)
        
        return money
            