class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        
        # for this problem you need to find the two biggest numbers and the smallest numbers
        # then take the product of the two biggest numbers 
        # take the product of the two smallest numbers
        # the difference between these two would be the maximum product difference. 

        
        firstMax = 0
        secondMax = 0
        
        firstLeast = 10000
        secondLeast = 10000
        
        for num in nums:
            if num > firstMax:
                secondMax = firstMax
                firstMax = num
            elif num > secondMax:
                secondMax = num
            
            if num < firstLeast:
                secondLeast = firstLeast
                firstLeast = num
            elif num < secondLeast:
                secondLeast = num
                
        print(f"firstMax = {firstMax} , secondMax = {secondMax}, firstLeast = {firstLeast} , secondLeast = {secondLeast}")  
        
#         for num in nums:
            
#             discardedSecondMaxValue = 0
            
#             if firstMax == 0 and secondMax == 0:
#                 firstMax = num
                
#             elif num > firstMax:
#                 discardedSecondMaxValue = secondMax
#                 secondMax = firstMax
#                 firstMax = num
                
#             elif num > secondMax:
#                 discardedSecondMaxValue = secondMax
#                 secondMax = num
                
#             if discardedSecondMaxValue != 0:
#                 if firstLeast == 10000 and secondLeast == 10000:
#                     firstLeast = discardedSecondMaxValue
#                 elif discardedSecondMaxValue < firstLeast:
#                     secondLeast = firstLeast
#                     firstLeast = discardedSecondMaxValue
#                 elif discardedSecondMaxValue < secondLeast:
#                     secondLeast = discardedSecondMaxValue
#             else:
#                 if num <= firstMax and num <= secondMax:
#                     if firstLeast == 10000 and secondLeast == 10000:
#                         firstLeast = num
#                     elif num < firstLeast:
#                         secondLeast = firstLeast
#                         firstLeast = num
#                     elif num < secondLeast:
#                         secondLeast = num
            
#         print(f"firstMax = {firstMax} , secondMax = {secondMax}, firstLeast = {firstLeast} , secondLeast = {secondLeast}")
        
#         if firstLeast == 10000 and secondLeast == 10000:
#             return 0
        
        return (firstMax * secondMax) - (firstLeast * secondLeast)