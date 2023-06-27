class Solution(object):
    
    def __init__(self):
        self.pastCalculationsMemory = {}
    
    def climbStairsRecursionWithMemo(self , step , n):
        
        if step > n:
            return 0
        
        if step == n:
            return 1
        
        if step in self.pastCalculationsMemory:
            return self.pastCalculationsMemory[step]
        
        self.pastCalculationsMemory[step] = self.climbStairsRecursionWithMemo(step + 1 , n ) + self.climbStairsRecursionWithMemo(step + 2 , n )
        return self.pastCalculationsMemory[step]
        
    
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        # got clarity after watching the following video 
        # https://www.youtube.com/watch?v=Y0lT9Fck7qI
        
        if n == 0:
            return 0
        
        return self.climbStairsRecursionWithMemo(0 , n )
        
    