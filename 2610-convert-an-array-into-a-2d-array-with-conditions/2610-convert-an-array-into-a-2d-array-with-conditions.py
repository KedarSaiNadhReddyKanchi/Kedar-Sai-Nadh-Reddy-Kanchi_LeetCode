class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashmap = {}
        unique_numbers_count = 0
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
                unique_numbers_count = unique_numbers_count + 1
            else:
                hashmap[num] = hashmap[num] + 1
        
        print(hashmap)
        print(unique_numbers_count)
        
        result = []
        while unique_numbers_count > 0:
            row = []
            for key in hashmap:
                if hashmap[key] != 0:
                    row.append(key)
                    hashmap[key] = hashmap[key] - 1
                    if hashmap[key] == 0:
                        unique_numbers_count = unique_numbers_count - 1
            result.append(row)
        
        print(result)
        return result
                
            
        