class Solution:
    def convert(self, s: str, numRows: int) -> str:
        slength = len(s)
        
        if numRows == 1 or numRows >= slength:
            return s
    
        stringcopy = [[] for _ in range(numRows)]
        #print(stringcopy)
        
        position = 0
        trend = "down"
        
        for letter in s:
            stringcopy[position].append(letter)
            if position == 0:
                trend = "down"
            elif position == (numRows - 1):
                trend = "up"
            
            if trend == "down":
                position = position + 1
            else:
                position = position - 1

        
        #print(stringcopy)
        return ''.join(''.join(row) for row in stringcopy)