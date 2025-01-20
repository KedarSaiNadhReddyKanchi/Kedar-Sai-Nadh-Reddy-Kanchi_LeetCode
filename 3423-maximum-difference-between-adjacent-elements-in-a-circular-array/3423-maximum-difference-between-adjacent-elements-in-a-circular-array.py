class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        last = nums[-1]
        position = 0
        preivous = None
        maximum_difference = 0
        for num in nums:
            if position == 0:
                difference = abs(num - last)
                maximum_difference = max(maximum_difference , difference)
            else:
                difference = abs(num - previous)
                maximum_difference = max(maximum_difference , difference)
            
            position = position + 1
            previous = num
        
        return maximum_difference