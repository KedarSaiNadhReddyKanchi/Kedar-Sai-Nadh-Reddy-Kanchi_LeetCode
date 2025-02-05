class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        map_A = {}
        map_B = {}
        # map_C = {}
        count = 0
        result = []

        for value_A, value_B in zip(A, B):
            map_A[value_A] = True
            if value_A in map_B:
                count = count + 1
                # map_C[value_A] = True
            
            map_B[value_B] = True
            if value_B in map_A:
                count = count + 1
                # map_C[value_B] = True
            
            # print(map_C)
            result.append(count)
        
        return result
            
