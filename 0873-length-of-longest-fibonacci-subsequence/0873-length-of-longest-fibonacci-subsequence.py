class Solution:
    def __init__(self):
        self.longest_length = 0
        self.arrmap = None
        self.arrmapSize = 0
    
    def recursion(self, first, second, size):
        third = first + second
        if third not in self.arrmap:
            if size >= 3:
                self.longest_length = max(self.longest_length , size)
            return
        
        self.recursion(second , third, (size + 1))
        return

    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        self.arrmap = set(arr)
        size = len(arr)
        for position , num in enumerate(arr):
            for index in range((position + 1) , size):
                self.recursion(num , arr[index], 2)
        return self.longest_length
        