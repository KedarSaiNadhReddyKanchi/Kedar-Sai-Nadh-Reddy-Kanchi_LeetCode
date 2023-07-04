class Solution:
    
    def __init__(self):
        self.adjacencyList = {}
        self.currentStack = []
        self.visitedNodes = {}
        self.checkFlag = False
        
    def updateAdjacencyList(self, vertex1 , vertex2):
        if vertex1 in self.adjacencyList:
            self.adjacencyList[vertex1].append(vertex2)
        else:
            self.adjacencyList[vertex1] = []
            self.adjacencyList[vertex1].append(vertex2)
    
    def createAdjacencyList(self, edges):
        for start , end in edges:
            self.updateAdjacencyList(start , end)
            self.updateAdjacencyList(end , start)
    
    def addNeighboursOntoTheStack(self , popped_node):
        for neighbour in self.adjacencyList[popped_node]:
            self.currentStack.append(neighbour)
                
    def intializeDataStructures(self , source):
        # load the source node on to the current stack to start
        self.visitedNodes[source] = True
        # add in the neighbours
        self.addNeighboursOntoTheStack(source)
    
    def findPath(self , destination):
        
        if len(self.currentStack) == 0:
            return self.checkFlag
        
        poppedNode = self.currentStack.pop()
        
        # base case 
        if poppedNode == destination:
            return True
        
        # add the neighbours only if the popped node is not in the visited stack
        if poppedNode not in self.visitedNodes:
            # add in the neighbours
            self.addNeighboursOntoTheStack(poppedNode)
            # add the popped node to the visited stack
            self.visitedNodes[poppedNode] = True
            # print(self.currentStack)
         
        return self.findPath(destination)
    
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if len(edges) == 0 and source == destination:
            return True
        
        self.createAdjacencyList(edges)
        # print(self.adjacencyList)
        self.intializeDataStructures(source)
        return self.findPath(destination)
        