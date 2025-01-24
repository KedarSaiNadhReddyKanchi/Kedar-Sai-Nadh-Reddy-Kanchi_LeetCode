class Solution:
    def __init__(self):
        self.adjacencyMap = {}
        self.safe_nodes = {}
        self.non_safe_nodes = {}
    
    def createAdjacencyMapOfGraph(self, graph):
        for node_index, connected_nodes_list in enumerate(graph):
            number_of_connected_nodes = len(connected_nodes_list)
            if number_of_connected_nodes == 0:
                self.safe_nodes[node_index] = True
            self.adjacencyMap[node_index] = connected_nodes_list
    
    def recursiveFunction(self, node_index, connected_nodes_list, visited_map):
        # base condition
        if node_index in self.safe_nodes:
            return True
        
        if node_index in self.non_safe_nodes:
            return False
        
        if node_index in visited_map:
            return False # loop encountered
        
        # go every path starting from this node and check if all the paths lead to a safe node
        # and while doing so check if the paths starting from the subsequent nodes in the path
        # also lead to a safe node and if so then mark that subsequent node as safe and return
        
        for connected_node_index in connected_nodes_list:
            is_safe = self.recursiveFunction(connected_node_index, self.adjacencyMap[connected_node_index], {**visited_map, node_index: True})
            if not is_safe:
                self.non_safe_nodes[node_index] = True
                return False
        
        self.safe_nodes[node_index] = True
        return True

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        self.createAdjacencyMapOfGraph(graph)
        print(self.safe_nodes)
        print(self.adjacencyMap)

        for node_index, connected_nodes_list in enumerate(graph):
            is_safe = self.recursiveFunction(node_index, connected_nodes_list, {})
            if is_safe:
                self.safe_nodes[node_index] = True
            else:
                self.non_safe_nodes[node_index] = True
        
        print("result post recursion")
        print("self.safe_nodes = " , self.safe_nodes)
        print("self.non_safe_nodes = " , self.non_safe_nodes)

        list_of_safe_nodes = sorted(list(self.safe_nodes.keys()))
        return list_of_safe_nodes