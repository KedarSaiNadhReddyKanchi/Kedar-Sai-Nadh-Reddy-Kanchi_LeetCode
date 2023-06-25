class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        hashmap = {}
        maxcountnum = -1
        maxcount = int(len(nums) / 2)
        
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
            
            if hashmap[num] > maxcount:
                maxcountnum = num
        
        return maxcountnum
                
        