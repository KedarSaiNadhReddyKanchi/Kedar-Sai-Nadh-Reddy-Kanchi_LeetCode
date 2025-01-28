class Solution:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.maximum = 0
        self.water_cells = {}
        self.processed_cell_with_maximum_count = {}

    def recursiveFunction(self, row , column, visited):
        # base condition -- if already cell has been processed
        # if (row , column) in self.processed_cell_with_maximum_count:
        #     return self.processed_cell_with_maximum_count[(row , column)]

        # get the adjacency cell positions
        same_row , right_column = row, column + 1
        same_row , left_column = row, column - 1
        top_row , same_column = row - 1, column
        bottom_row , same_column = row + 1, column

        # consume fish at that cell completely
        number_of_fish_in_this_cell = self.water_cells[(row, column)]
        max_fish_count_from_this_cell = number_of_fish_in_this_cell
        visited.add((row , column))

        # go to the right cell if water cell and within grid boundary
        if (right_column < self.columns) and ((same_row , right_column) in self.water_cells) and ((same_row , right_column) not in visited):
            returned_max_fish_count_from_moving_in_the_right_direction = self.recursiveFunction(same_row , right_column, visited)
            highest_count_to_be_reached_from_moving_in_the_right_direction = number_of_fish_in_this_cell + returned_max_fish_count_from_moving_in_the_right_direction
            max_fish_count_from_this_cell = max(max_fish_count_from_this_cell , highest_count_to_be_reached_from_moving_in_the_right_direction)
        
        # go to the left cell if water cell and within grid boundary
        if (left_column < self.columns) and ((same_row , left_column) in self.water_cells) and ((same_row , left_column) not in visited):
            returned_max_fish_count_from_moving_in_the_left_direction = self.recursiveFunction(same_row , left_column, visited)
            highest_count_to_be_reached_from_moving_in_the_left_direction = number_of_fish_in_this_cell + returned_max_fish_count_from_moving_in_the_left_direction
            max_fish_count_from_this_cell = max(max_fish_count_from_this_cell , highest_count_to_be_reached_from_moving_in_the_left_direction)

        # go to the top cell if water cell and within grid boundary
        if (top_row < self.rows) and ((top_row , same_column) in self.water_cells) and ((top_row , same_column) not in visited):
            returned_max_fish_count_from_moving_in_the_top_direction = self.recursiveFunction(top_row , same_column, visited)
            highest_count_to_be_reached_from_moving_in_the_top_direction = number_of_fish_in_this_cell + returned_max_fish_count_from_moving_in_the_top_direction
            max_fish_count_from_this_cell = max(max_fish_count_from_this_cell , highest_count_to_be_reached_from_moving_in_the_top_direction)

        # go to the bottom cell if water cell and within grid boundary
        if (bottom_row < self.rows) and ((bottom_row , same_column) in self.water_cells) and ((bottom_row , same_column) not in visited):
            returned_max_fish_count_from_moving_in_the_bottom_direction = self.recursiveFunction(bottom_row , same_column, visited)
            highest_count_to_be_reached_from_moving_in_the_bottom_direction = number_of_fish_in_this_cell + returned_max_fish_count_from_moving_in_the_bottom_direction
            max_fish_count_from_this_cell = max(max_fish_count_from_this_cell , highest_count_to_be_reached_from_moving_in_the_bottom_direction)
        
        self.processed_cell_with_maximum_count[(row, column)] = max_fish_count_from_this_cell
        self.maximum = max(self.maximum , max_fish_count_from_this_cell)
        return max_fish_count_from_this_cell

    def findMaxFish(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.columns = len(grid[0])

        for row_number , row in enumerate(grid):
            for column_number, cell_value in enumerate(row):
                if cell_value > 0:
                    # then a water cell with fish
                    self.water_cells[(row_number, column_number)] = cell_value
        print(self.water_cells)

        for cell_position in self.water_cells:
            row_number , column_number = cell_position
            visited = set()
            visited.add((row_number , column_number))
            self.recursiveFunction(row_number , column_number, visited)
        
        print(self.processed_cell_with_maximum_count)
        return self.maximum