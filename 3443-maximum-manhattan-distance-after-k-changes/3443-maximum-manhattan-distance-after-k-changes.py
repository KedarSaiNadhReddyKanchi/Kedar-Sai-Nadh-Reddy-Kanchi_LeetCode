class Solution:
    def __init__(self):
        self.max_manhattan_distance = 0
        self.x = 0
        self.y = 0
    
    def calculateManhattanDistance(self , direction):
        delta = {
            "N": [0 , 1],
            "S": [0 , -1],
            "W": [-1 , 0],
            "E": [1 , 0],
        }

        delta_x , delta_y = delta[direction]
        self.x , self.y = (self.x + delta_x) , (self.y + delta_y)
        distance = abs(self.x) + abs(self.y)
        self.max_manhattan_distance = max(self.max_manhattan_distance , distance)

    def maxDistance(self, s: str, k: int) -> int:
        # try to move in as much as possible in one direction to result in the highest distance from the origin
        # since we do not know at which point we might encounter the highest distance from the origin
        # we need to try all possible combinations with limited (k) changes
        # but it is really impossible to determine which exact leters in the string are to be changed 
            # to result in the best possible answer - we have to try all combinations
        
        # so take the quandrant system where 
            # x , y are positive in the first quadrant (NE - North East)
            # x is negative , y is positive in the second quadrant (NW - North West)
            # x , y is negative in the third quadrant (SW - South West)
            # x is positive , y is negative in the fourth quadrant (SE - South East)
        
        # so we need to make sure to go as much as possible in the four cases - NE (1) , NW (2), SW (3) and SE (4)
            # so for the 1st quadrant - convert all the S --> N and all W --> E resulting in (NE)
            # so for the 2nd quadrant - convert all the S --> N and all E --> W resulting in (NW)
            # so for the 3rd quadrant - convert all the N --> S and all E --> W resulting in (SW)
            # so for the 4th quadrant - convert all the N --> S and all W --> E resulting in (SE)
        
        # case 1 - get all NE
        temp = k
        for direction in s:
            if direction == "N" or direction == "E":
                self.calculateManhattanDistance(direction)
            elif direction == "S" and temp > 0:
                self.calculateManhattanDistance("N")
                temp = temp - 1
            elif direction == "W" and temp > 0:
                self.calculateManhattanDistance("E")
                temp = temp - 1
            else:
                self.calculateManhattanDistance(direction)
        
        self.x = 0
        self.y = 0
        temp = k
        # case 2 - get all NW
        for direction in s:
            if direction == "N" or direction == "W":
                self.calculateManhattanDistance(direction)
            elif direction == "S" and temp > 0:
                self.calculateManhattanDistance("N")
                temp = temp - 1
            elif direction == "E" and temp > 0:
                self.calculateManhattanDistance("W")
                temp = temp - 1
            else:
                self.calculateManhattanDistance(direction)
        
        self.x = 0
        self.y = 0
        temp = k
        # case 3 - get all SW
        for direction in s:
            if direction == "S" or direction == "W":
                self.calculateManhattanDistance(direction)
            elif direction == "N" and temp > 0:
                self.calculateManhattanDistance("S")
                temp = temp - 1
            elif direction == "E" and temp > 0:
                self.calculateManhattanDistance("W")
                temp = temp - 1
            else:
                self.calculateManhattanDistance(direction)
        
        self.x = 0
        self.y = 0
        temp = k
        # case 4 - get all SE
        for direction in s:
            if direction == "S" or direction == "E":
                self.calculateManhattanDistance(direction)
            elif direction == "N" and temp > 0:
                self.calculateManhattanDistance("S")
                temp = temp - 1
            elif direction == "W" and temp > 0:
                self.calculateManhattanDistance("E")
                temp = temp - 1
            else:
                self.calculateManhattanDistance(direction)
        
        return self.max_manhattan_distance

            

