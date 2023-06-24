import itertools as IT
class Solution(object):
    
    def __init__(self):
        self.keyMap = {}
        
    def evaluateQueries(self , queries):
        results = []
        for query in queries:
            character1 = query[0]
            character2 = query[1]
            
            if character1 not in self.keyMap:
                results.append(float(-1))
            elif character2 not in self.keyMap:
                results.append(float(-1))
            elif character1 == character2:
                results.append(float(1))
            else:
                character1_rootNode , character1_weight = self.find(character1)
                character2_rootNode , character2_weight = self.find(character2)
                # this is because the query can only be executed
                # if both the characters share the same root node
                if character1_rootNode == character2_rootNode:
                    results.append(character1_weight / character2_weight)
                else:
                    results.append(float(-1))
        return results
    
    def find(self , node):
        if node not in self.keyMap:
            # initially if the node is not there
            # then we need to add itself as the parent node with weight = 1
            self.keyMap[node] = [node , 1]
        
        # if the node in question is already in the key map
        # then we extract the stored root node and the root weight
        root_node , root_weight = self.keyMap[node]
        
        if root_node != node:
            new_root_node , new_root_weight = self.find(root_node)
            self.keyMap[node] = [new_root_node , new_root_weight * root_weight]
        
        return self.keyMap[node]
    
            
    def union(self , character1 , character2 , value = 1):
        character1_rootNode , character1_weight = self.find(character1)
        character2_rootNode , character2_weight = self.find(character2)
        
        if character1_rootNode != character2_rootNode:
            updated_weight = (character2_weight / character1_weight) * value
            self.keyMap[character1_rootNode] = [character2_rootNode , updated_weight]
        
    def updateKeyMap(self , equations , values):
        for equation , value in IT.izip(equations , values):
            character1 = equation[0]
            character2 = equation[1]
            # character1 is divisible by character2
            # so the root of character1 should be root of character2
            self.union(character1 , character2 , value)
            
    
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        
        self.updateKeyMap(equations , values)
        print(self.keyMap)
        
        results = self.evaluateQueries(queries)
        print(results)
        return results
        
        
        