class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #*********************************************************
        # need to do this again after learning dyanmic programming
        #**********************************************************
        
        # for now I am doing this problem iteratively using queues
        queue = []
        queue.append((sr , sc))
        m = len(image)
        n = len(image[0])
        memo = {}
        # print("current queue")
        # print(queue)
        
        while (len(queue) != 0):
            row , column = queue.pop(0)
            x1 , y1 = row , column - 1
            x2 , y2 = row , column + 1
            x3 , y3 = row - 1 , column
            x4 , y4 = row + 1 , column
            list_of_four_points = [[x1 , y1] , [x2 , y2] , [x3 , y3] , [x4 , y4]]
            
            for row_point, column_point in list_of_four_points:
                if (row_point >= 0) and (column_point >= 0):
                    if ((row_point < m) and (column_point < n)):
                        if (image[row][column] == image[row_point][column_point]):
                            stringpointcheck = "" + str(row_point) + "" + str(column_point)
                            if stringpointcheck not in memo:
                                queue.append((row_point , column_point))
            
            # print("current queue")
            # print(queue)        
            
            image[row][column] = color
            
            stringpoint = "" + str(row) + "" + str(column)
            memo[stringpoint] = "visited"
        
        # print(image)
        return image
        
        