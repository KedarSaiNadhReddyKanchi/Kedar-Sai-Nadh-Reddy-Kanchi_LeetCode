class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        position = 1
        complete_rows_count = 0
        while n > 0:
            n = n - position
            position = position + 1
            if n >= 0:
                complete_rows_count = complete_rows_count + 1

        
        return complete_rows_count
            
        