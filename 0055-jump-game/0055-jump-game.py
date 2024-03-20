class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        end_point = len(nums) - 1
        index = end_point - 1
        intermediary_point = end_point
        
        while (index >= 0):
            value = nums[index]
            # print(f"value = {value} -- index = {index}")
            if ((index + value) >= intermediary_point):
                intermediary_point = index
                # print(f"intermediary_point = {intermediary_point} -- index = {index}")
            index = index - 1
            
        if intermediary_point == 0:
            return True
        
        return False
            
        