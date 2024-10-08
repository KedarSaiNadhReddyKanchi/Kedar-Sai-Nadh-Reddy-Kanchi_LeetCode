class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        start = 0
        maxLength = 0
        numsLength = len(nums)
        end = numsLength - 1

        while start < numsLength:
            if nums[start] % 2 != 0:
                start = start + 1
            elif nums[start] > threshold:
                start = start + 1
            else:
                left = start
                while ((start < end) and (nums[start] % 2 != nums[start + 1] % 2) and (max(nums[start], nums[start + 1]) <= threshold)):
                    start = start + 1
                maxLength = max(maxLength, start - left + 1)
                start = start + 1
        
        return maxLength

        