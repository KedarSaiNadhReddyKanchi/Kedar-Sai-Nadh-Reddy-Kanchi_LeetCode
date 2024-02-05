class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        hash_map = {
            "true_destination_city": {},
            "other_cities": {}
        }
        
        
        for path in paths:
            startingCity = path[0]
            destinationCity = path[1]
            
            if startingCity in hash_map["true_destination_city"]:
                del hash_map["true_destination_city"][startingCity]
                hash_map["other_cities"][startingCity] = "not"
            else:
                hash_map["other_cities"][startingCity] = "not"
                
            
            if destinationCity not in hash_map["other_cities"]:
                hash_map["true_destination_city"][destinationCity] = 1
        
        first_key = next(iter(hash_map["true_destination_city"])) 
        return first_key
            
            
                
                
                
                
            
        