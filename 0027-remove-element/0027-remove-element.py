class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        start = 0 
        length = len(nums)
        
        while start < len(nums):
            if nums[start] == val:
                del nums[start]
            else:
                start = start + 1
        
        return len(nums) 
        