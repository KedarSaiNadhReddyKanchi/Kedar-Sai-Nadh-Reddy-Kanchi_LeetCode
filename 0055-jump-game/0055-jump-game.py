class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        nums_length = len(nums)
        end = nums_length - 1
        start = 0 
        last_reachable_index = end
        
        for position in range ((end - 1), -1, -1):
            max_reachable_position = position + nums[position]
            if max_reachable_position >= last_reachable_index:
                last_reachable_index = position
        
        print(last_reachable_index)
        if (last_reachable_index == 0):
            return True
    
        return False
            
        