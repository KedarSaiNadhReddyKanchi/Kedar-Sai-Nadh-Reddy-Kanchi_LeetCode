class Solution:
    def convert(self, s: str, numRows: int) -> str:

        slength = len(s)
        
        if numRows == 1 or numRows >= slength:
            return s
           
        slist = list(s)
        rows = numRows
        columns = slength
        if columns == 0:
            columns = 1
        arr = [[] for _ in range(rows)]
        for i in range(rows):
            arr[i] = [None] * columns
        
        start = 0
        end = 0
        trend = "down"
        flag = False
        
        for letter in slist:
            if start == (numRows):
                trend = "up"
                start = start - 1
            
            elif start == 0:
                trend = "down"
                if flag:
                    start = start + 1
                
            if trend == "down":
                arr[start][end] = letter
                start = start + 1
            
            elif trend == "up":
                start = start - 1
                if start < 0:
                    start = 0
                end = end + 1
                arr[start][end] = letter
        
            flag = True
        
        finalstring = ""
        rowcount  = 0
        while rowcount < numRows:
            temp = 0
            while temp <= end:
                letter = arr[rowcount][temp]
                if letter is not None:
                    finalstring = finalstring + letter
                temp = temp + 1
            rowcount = rowcount + 1

        return finalstring
                
                
            
        