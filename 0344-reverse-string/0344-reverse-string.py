class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        start = 0
        end  = len(s) - 1
        
        while start <= end:
            tempvalue = s[start]
            s[start] = s[end]
            s[end] = tempvalue
            start = start + 1
            end = end - 1
        
        return s
        