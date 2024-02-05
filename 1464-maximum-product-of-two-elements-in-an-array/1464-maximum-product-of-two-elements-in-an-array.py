class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        firstMax = 0
        secondMax = 0
        
        for number in nums:
            if firstMax == 0 and secondMax == 0:
                firstMax = number;
            elif number > firstMax:
                secondMax = firstMax 
                firstMax = number
            elif number > secondMax:
                secondMax = number
        
        print("firstMax = %d and secondMax = %d", firstMax , secondMax )
        return (firstMax - 1) * (secondMax - 1)        