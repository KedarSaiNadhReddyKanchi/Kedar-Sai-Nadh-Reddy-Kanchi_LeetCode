class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start = 0
        end  = len(s) - 1
        
        while start <= end:
            tempvalue1 = s[start]
            tempvalue2 = s[end]
            s[start] = tempvalue2
            s[end] = tempvalue1
            start = start + 1
            end = end - 1
        
        return s
        