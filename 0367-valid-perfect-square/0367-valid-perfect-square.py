class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        if num <= 10:
            if num in [1,4,9]:
                return True
            else:
                return False
        
        start = 1
        end = num
        
        while start < end:
            total = start + end
            mid = (int)(total / 2)
            if mid * mid == num:
                return True
            else:
                if mid * mid < num:
                    start = mid + 1
                else:
                    end = mid
        
        return False
        