class Solution:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.row_plane = {}
        self.column_plane = {}
        self.visited = set()

    def recursion(self, x , y):
        for col in self.row_plane[x]:
            if (x , col) not in self.visited:
                self.visited.add((x , col))
                self.recursion(x , col)
        
        for row in self.column_plane[y]:
            if (row , y) not in self.visited:
                self.visited.add((row , y))
                self.recursion(row , y)

    def removeStones(self, stones: List[List[int]]) -> int:
        number_of_stones = 0
        for x , y in stones:
            self.rows = max(self.rows , x)
            self.columns = max(self.columns , y)

            if x not in self.row_plane:
                self.row_plane[x] = set()
            
            if y not in self.row_plane[x]:
                self.row_plane[x].add(y)
            
            if y not in self.column_plane:
                self.column_plane[y] = set()
            
            if x not in self.column_plane[y]:
                self.column_plane[y].add(x)
            
            number_of_stones = number_of_stones + 1
        
        self.rows = self.rows + 1
        self.columns = self.columns + 1

        connected_clusters = 0

        for x , y in stones:
            if (x , y) not in self.visited:
                self.visited.add((x , y))
                self.recursion(x , y)
                connected_clusters = connected_clusters + 1
        
        print(number_of_stones , connected_clusters)
        return (number_of_stones - connected_clusters)