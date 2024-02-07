class Solution:
    def isPathCrossing(self, path: str) -> bool:
        
        hash_map = {
            "0,0": 1
        }
        
        x = 0
        y = 0
        overlap = False
        
        for direction in path:
            if direction == "N":
                y = y + 1
            elif direction == "E":
                x = x + 1
            elif direction == "S":
                y = y - 1
            else:
                x = x - 1
            
            x_temp = x
            y_temp = y
            point = "" + str(x_temp) + "," + str(y_temp)
            if point not in hash_map:
                hash_map[point] = 1
            else:
                overlap = True
                break
        
        return overlap
            
            
                
        