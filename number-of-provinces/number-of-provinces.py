class Solution(object):
    
    def createRootArray(self, num_cities):
        self.root = [i for i in range(num_cities)]
        self.rank = [1] * num_cities
        self.count = num_cities
            
    def find(self, node):
        if node == self.root[node]:
            return node
        self.root[node] = self.find(self.root[node])
        return self.root[node]
    
    def union(self, node1, nodeY):
        root1 = self.find(node1)
        rootY = self.find(nodeY)
        if root1 != rootY:
            if self.rank[root1] > self.rank[rootY]:
                self.root[rootY] = root1
            elif self.rank[root1] < self.rank[rootY]:
                self.root[root1] = rootY
            else:
                self.root[rootY] = root1
                self.rank[root1] = self.rank[root1] + 1
            self.count = self.count - 1
                
    def total_number_of_root_nodes(self):
        count = 0
        hash_map = {}
        for node in self.root:
            if node in hash_map:
                continue
            else:
                hash_map[node] = node
                count = count + 1
        return count
                
    
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        self.createRootArray(len(isConnected))
        
        for position1 in range(len(isConnected)):
            for position2 in range(len(isConnected[position1])):
                if isConnected[position1][position2] == 1:
                    self.union(position1 , position2)
        
        print(self.root)
        print(self.total_number_of_root_nodes())
        print(self.count)
        return self.count