class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        start = 0
        end = len(nums) - 1
        position = -2
        
        while start <= end:
            mid = int((start + end + 1) / 2)
            if nums[mid] == target:
                position = mid
                break
            elif nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                continue
        
        if position >=0:
            return position
        return -1
            