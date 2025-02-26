class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        # the absolute subarray maximum can either come from 
            # the maximum positive subarray sum (or)
            # the least possible minimum negative subarray sum
        
        maxSum = None
        maxEnding = None
        for num in nums:
            if maxSum is None and maxEnding is None:
                maxSum = num
                maxEnding = num
            else:
                maxEnding = max(maxEnding + num , num)
                maxSum = max(maxSum , maxEnding)
        
        # print(maxSum)

        minSum = None
        minEnding = None
        for num in nums:
            if minSum is None and minEnding is None:
                minSum = num
                minEnding = num
            else:
                minEnding = min(minEnding + num , num)
                minSum = min(minSum, minEnding)
        
        # print(minSum)

        result = max(abs(maxSum), abs(minSum))
        return result
