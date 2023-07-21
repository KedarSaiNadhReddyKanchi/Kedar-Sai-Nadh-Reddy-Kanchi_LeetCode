class Solution:
    
    def __init__(self):
        self.adjacencyList = {}
        
    def createAdjacencyList(self, equations, values):
        for index, equation in enumerate(equations):
            node1, node2 = equation
            value = values[index]
            
            if node1 not in self.adjacencyList:
                self.adjacencyList[node1] = []
            self.adjacencyList[node1].append([node2 , value])
            
            if node2 not in self.adjacencyList:
                self.adjacencyList[node2] = []
            self.adjacencyList[node2].append([node1 , (1 / value)])
            
    def dfs(self, source, target):
        if source not in self.adjacencyList:
            return -1
        if target not in self.adjacencyList:
            return -1
        if source == target:
            return 1
        
        neighbours_list = []
        visited = {}
        
        neighbours_list.append([source , 1])
        # starting from the source node with the initial running product of the edges weights
        visited[source] = True
        
        while len(neighbours_list) > 0:
            popped_node =  neighbours_list.pop(0)
            node , running_weight = popped_node
            if node == target:
                return running_weight
            for neighbour , weight in self.adjacencyList[node]:
                if neighbour not in visited:
                    neighbours_list.append([neighbour , running_weight * weight])
                    visited[neighbour] = True
        return -1
        
                
            
            
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        self.createAdjacencyList(equations , values)
        
        results = []
        for query in queries:
            results.append(self.dfs(query[0] , query[1]))
        return results
        
        