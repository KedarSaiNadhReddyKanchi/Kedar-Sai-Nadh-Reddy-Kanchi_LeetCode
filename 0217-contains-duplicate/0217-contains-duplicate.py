class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hash_map = {}
        for num in nums:
            if num in hash_map:
                return True
            else:
                hash_map[num] = num
        
        return False
            
        