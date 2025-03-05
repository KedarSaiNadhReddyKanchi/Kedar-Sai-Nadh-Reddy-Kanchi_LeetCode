class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        
        previous_value = 1
        temp = 2
        while temp <= n:
            # at one point you can color 4 cells 
            colored_cells_at_temp = ((temp - 1) * 4) + previous_value
            previous_value = colored_cells_at_temp
            temp = temp + 1
        
        return previous_value