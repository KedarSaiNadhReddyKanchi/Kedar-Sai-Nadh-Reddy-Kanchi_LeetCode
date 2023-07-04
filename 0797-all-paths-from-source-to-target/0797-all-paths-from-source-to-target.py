class Solution:
    
    def __init__(self):
        self.visited = {}
        self.paths = []
    
    def findAllPaths(self , graph , source , destination , current_path):
        current_path.append(source)
        self.visited[source] = True
        
        if source == destination:
            self.paths.append(current_path.copy())
        else:
            # implement a recursive call stack
            for neighbour in graph[source]:
                if ((neighbour not in self.visited) or (self.visited[neighbour] == False)):
                    self.findAllPaths(graph , neighbour , destination , current_path)
        
        current_path.pop()
        self.visited[source] = False
        
            
    
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        source = 0
        destination = len(graph) - 1
        current_path = []
        self.findAllPaths(graph , source , destination , current_path)
        return (self.paths)
        