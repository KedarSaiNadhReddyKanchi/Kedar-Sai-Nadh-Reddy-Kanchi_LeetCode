from collections import deque
class Solution:
    def check(self, nums: List[int]) -> bool:
        initial_array = sorted(nums)
        print(nums)
        print(initial_array)
        
        initial_starting_value = initial_array[0]
        initial_starting_position = 0
        new_position = None
        numsLength = len(nums)
        # print(new_position != initial_starting_position)
        
        while ((new_position != initial_starting_position)):
            popped_value = initial_array[0]
            del initial_array[0]
            initial_array.append(popped_value)
            if new_position is None:
                new_position = numsLength - 1
            else:
                new_position = new_position - 1
            
            if initial_array == nums:
                return True
            
        return False
        