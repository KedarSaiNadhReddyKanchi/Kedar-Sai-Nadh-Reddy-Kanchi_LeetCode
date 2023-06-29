class DSU:
    
    def __init__(self):
        self.root = {}
        self.rank = {}
        
    def find(self, index):
        # the find method accepts an index as a parameter
        # this is to group all the indices present in the pairs parameter into clusters
        
        if index not in self.root:
            self.root[index] = index
            self.rank[index] = 1
            return index
        else:
            temp_root = index
            while temp_root != self.root[temp_root]:
                self.root[temp_root] = self.root[self.root[temp_root]]
                temp_root = self.root[temp_root]
            return temp_root
    
    def union(self, i , j):
        # the union function accepts two indices from the pairs paramters = pairs[i][0] and pairs[i][1]
        root_i = self.find(i)
        root_j = self.find(j)
        
        if root_i != root_j:
            if self.rank[root_i] >= self.rank[root_j]:
                self.root[root_j] = root_i
                self.rank[root_i] = self.rank[root_i] + self.rank[root_j]
            else:
                self.root[root_i] = root_j
                self.rank[root_j] = self.rank[root_j] + self.rank[root_i]
    
    def get_clusters(self):
        
        clusters = {}
        
        for key , value in self.root.items():
            parent = self.find(value)
            if parent not in clusters:
                clusters[parent] = {key}
            else:
                clusters[parent].add(key)
        
        return clusters

class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        
        dsu = DSU()
        
        for a , b in pairs:
            dsu.union(a , b)
        
        clusters = dsu.get_clusters()
        new_string_order = {}
        
        for cluster in clusters.values():
            chars = sorted([s[i] for i in cluster])
            indices = sorted(cluster)
            
            for idx , char in zip(indices , chars):
                new_string_order[idx] = char
        
        final_str = []
        for i in range(len(s)):
            if i in new_string_order:
                final_str.append(new_string_order[i])
            else:
                final_str.append(s[i])
                
        return "".join(final_str)
                
                


        