class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        prevPoint_start , prevPoint_end = coordinates[0]
        second_point_start , second_point_end = coordinates[1]
        slope = None
        
        intial_deltaY = second_point_end - prevPoint_end
        intial_deltaX = second_point_start - prevPoint_start
        if intial_deltaX == 0:
            slope = -1
        else:
            slope = (intial_deltaY / intial_deltaX)
        
        print("initial slope is = " , slope)
        
        for position , point in enumerate(coordinates):
            if position > 1:
                current_start_point , current_end_point = point
                deltaY = current_end_point - prevPoint_end
                deltaX = current_start_point - prevPoint_start
                if deltaX == 0 and slope == -1:
                    continue
                elif deltaX == 0 and slope != -1:
                    return False
                else:
                    new_slope = (deltaY / deltaX)
                    if new_slope == slope:
                        continue
                    else:
                        return False
        
        return True
                
                        
