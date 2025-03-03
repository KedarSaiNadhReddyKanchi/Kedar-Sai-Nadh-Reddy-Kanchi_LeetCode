class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        result = [0] * len(nums)
        result_pointer = 0

        for position , num in enumerate(nums):
            if position > 0:
                previous_value = nums[position - 1]
                current_value = nums[position]
                if previous_value == current_value:
                    nums[position - 1] = previous_value * 2
                    nums[position] = 0
                    if (previous_value * 2) != 0:
                        result[result_pointer] = previous_value * 2
                        result_pointer = result_pointer + 1
                else:
                    if previous_value != 0:
                        result[result_pointer] = previous_value
                        result_pointer = result_pointer + 1
        
        if nums[-1] != 0:
            result[result_pointer] = nums[-1]
        
        return result
