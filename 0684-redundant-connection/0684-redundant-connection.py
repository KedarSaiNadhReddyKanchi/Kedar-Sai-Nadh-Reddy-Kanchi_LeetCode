class Solution:
    def checkIfGraphConnected(self, node, adjacencyMap, number_of_nodes, visited_nodes):
        # add this node as visited along the path and return this set
        visited_nodes.add(node)
        
        for connected_node in adjacencyMap[node]:
            if connected_node not in visited_nodes:
                returned_visited_set = self.checkIfGraphConnected(connected_node, adjacencyMap, number_of_nodes, visited_nodes)
                visited_nodes = visited_nodes | returned_visited_set
        
        return visited_nodes

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        number_of_nodes = len(edges)
        adjacencyMap = {}
        for node in range(number_of_nodes):
            adjacencyMap[node + 1] = {}
        # print(adjacencyMap)

        for node_a , node_b in edges:
            adjacencyMap[node_a][node_b] = True
            adjacencyMap[node_b][node_a] = True
        print(adjacencyMap)

        position = number_of_nodes - 1
        while position >= 0:
            # retrieve the edge at the position while iterating from the last
            node_a , node_b = edges[position]

            # delete the edge from both those nodes
            del adjacencyMap[node_a][node_b]
            del adjacencyMap[node_b][node_a]
            
            # now check if you can reach all the nodes from 1 to n with the resultant graph map
            visited_nodes = self.checkIfGraphConnected(1, adjacencyMap, number_of_nodes, set())
            length_of_visited_nodes = len(visited_nodes)
            if length_of_visited_nodes == number_of_nodes:
                return [node_a , node_b]
            else:
                # add back the deleted node
                adjacencyMap[node_a][node_b] = True
                adjacencyMap[node_b][node_a] = True

                # and decrement the while loop pointer to move to the next edge 
                position = position - 1
            
