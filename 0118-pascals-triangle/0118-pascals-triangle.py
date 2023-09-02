class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        if numRows == 0:
            return []
        
        if numRows == 1:
            return [[1]]
        
        if numRows == 2:
            return [[1] , [1,1]]
        
        result = [[1] , [1 , 1]]
        hashmap = {
            0: {
                0: 1
            }, 
            1: {
                0: 1,
                1: 1
            }
        }
        
        for position in range(2 , numRows):
            hashmap[position] = {}
            temp_list_for_current_position = []
            for index in range(0 , (position + 1)):
                if index == 0:
                    hashmap[position][0] = 1
                    temp_list_for_current_position.append(1)
                elif index == position:
                    hashmap[position][position] = 1
                    temp_list_for_current_position.append(1)
                else:
                    first_top_point = [position - 1 , index - 1]
                    second_top_point = [position - 1, index]
                    value1 = hashmap[first_top_point[0]][first_top_point[1]]
                    value2 = hashmap[second_top_point[0]][second_top_point[1]]
                    new_value = value1 + value2
                    hashmap[position][index] = new_value
                    temp_list_for_current_position.append(new_value)
            result.append(temp_list_for_current_position)
        
        # print(hashmap)
        # print(result)
        return result
                    
        