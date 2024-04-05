class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        index = len(s) - 1
        total = 0
        
        while index >= 0:
            if s[index] == " ":
                if total == 0:
                    index = index - 1
                    continue
                else:
                    return total
            else:
                total = total + 1
            
            index = index - 1
        
        return total
            