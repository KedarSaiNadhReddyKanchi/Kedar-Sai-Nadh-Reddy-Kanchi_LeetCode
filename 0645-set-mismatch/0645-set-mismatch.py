class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        totalLength = len(nums)
        largestNumber = totalLength
        
        hashmap = {}
        start = 1
        while start <= largestNumber:
            hashmap[start] = False
            start = start + 1
        
        repeatedNumber = -1
        for num in nums:
            if num in hashmap:
                if hashmap[num] == False:
                    del hashmap[num]
            else:
                repeatedNumber = num
        
        result = [repeatedNumber]
        for key in hashmap.keys():
            result.append(key)
        return result