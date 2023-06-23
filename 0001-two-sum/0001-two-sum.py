class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        hash_map = {}
        position = 0
        complement = 0
        for num in nums:
            complement = target - num
            if complement in hash_map:
                break
            else:
                hash_map[num] = position
            position = position + 1
        
        return [hash_map[complement] , position]
