class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0:
            return 0
        
        stop_point = int(x / 2)
        start = 2
        
        while start <= stop_point:
            if start * start > x:
                break
            start = start + 1
        
        return start - 1
        