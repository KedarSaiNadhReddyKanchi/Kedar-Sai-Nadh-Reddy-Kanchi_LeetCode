class Solution:
    def __init__(self):
        self.hashmap = {}
        self.sharingCellBoundariesAlongTheRow = 0
        self.previousIslandCell = -1
        self.sharingCellBoundariesInThePreviousRows = 0
    
    def updateTheVisitedCells(self, rowIndex, cellIndex):
        if rowIndex not in self.hashmap:
            self.hashmap[rowIndex] = {}
            self.hashmap[rowIndex][cellIndex] = 1
        else:
            self.hashmap[rowIndex][cellIndex] = 1
    
    def countContigousIslandCellsInRow(self, cellIndex):
        if self.previousIslandCell == -1:
            return (self.sharingCellBoundariesAlongTheRow + 0)
        
        elif self.previousIslandCell == (cellIndex - 1):
            return (self.sharingCellBoundariesAlongTheRow + 1)
        
        else:
            return (self.sharingCellBoundariesAlongTheRow + 0)
    
    def commonCellsInThePreviousRows(self, rowIndex , cellIndex):
        abovecell_Row = rowIndex - 1
        if abovecell_Row in self.hashmap: 
            if cellIndex in self.hashmap[abovecell_Row]:
                return (self.sharingCellBoundariesInThePreviousRows + 1)
            else:
                return (self.sharingCellBoundariesInThePreviousRows + 0)
        else:
            return (self.sharingCellBoundariesInThePreviousRows + 0)
    
    def calculateRowPerimeter(self):
        
        normal_perimeter_value = self.islandCount * 4
        
        if self.sharingCellBoundariesAlongTheRow == 0 and self.sharingCellBoundariesInThePreviousRows == 0:
            return normal_perimeter_value
        
        if self.sharingCellBoundariesAlongTheRow > 0:
            normal_perimeter_value = normal_perimeter_value - (self.sharingCellBoundariesAlongTheRow * 2)
        
        if self.sharingCellBoundariesInThePreviousRows > 0:
            normal_perimeter_value = normal_perimeter_value - (self.sharingCellBoundariesInThePreviousRows * 2)
        
        return normal_perimeter_value
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for rowIndex, row in enumerate(grid):
            
            self.sharingCellBoundariesAlongTheRow = 0
            self.sharingCellBoundariesInThePreviousRows = 0
            self.previousIslandCell = -1
            self.islandCount = 0
            
            for cellIndex, cell in enumerate(row):
                if cell == 1:
                    self.sharingCellBoundariesAlongTheRow = self.countContigousIslandCellsInRow(cellIndex)
                    self.sharingCellBoundariesInThePreviousRows = self.commonCellsInThePreviousRows(rowIndex, cellIndex)
                    self.updateTheVisitedCells(rowIndex, cellIndex)
                    self.previousIslandCell = cellIndex
                    self.islandCount = self.islandCount + 1
                    
            print(self.sharingCellBoundariesAlongTheRow)
            print(self.sharingCellBoundariesInThePreviousRows)
            
            total_perimeter_for_the_row = self.calculateRowPerimeter()
            total = total + total_perimeter_for_the_row
            print(f"running total = {total}")
            print()
            
        return total