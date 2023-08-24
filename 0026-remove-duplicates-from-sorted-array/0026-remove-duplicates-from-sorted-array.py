class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        position = 1
        length = len(nums)
        tochangeposition = 1
        count = 1
        
        if length == 1:
            return length
        
        while position < length:
            currentValue = nums[position]
            prevValue = nums[position - 1]
            
            if currentValue != prevValue:
                nums[tochangeposition] = currentValue
                tochangeposition = tochangeposition + 1
                count = count + 1
            
            position = position + 1
        
        return count
                