class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s
        
        slist = list(s)
        # print(slist)
        slength = len(s)
           
   
        rows = numRows
        columns = slength
        if columns == 0:
            columns = 1
        arr = [[] for _ in range(rows)]
        for i in range(rows):
            arr[i] = [None] * columns
        # print(arr)
        # print()
        
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
                # print(f"trend = {trend} and start = {start} and end = {end} and letter = {letter}")
                # print()
                arr[start][end] = letter
                start = start + 1
            
            elif trend == "up":
                start = start - 1
                if start < 0:
                    start = 0
                end = end + 1
                # print(f"trend = {trend} and start = {start} and end = {end} and letter = {letter}")
                # print()
                arr[start][end] = letter
        
            # print(arr)
            # print()
            flag = True
        
        # print(f"last column value = {end}")
        
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
        
        # print(finalstring)
        return finalstring
                
                
            
        