class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        sortedlist = sorted(nums)
        keyvalueCountList = []
        
        prevnum = None
        count = 0
        for number in sortedlist:
            if prevnum == None:
                prevnum = number
                count = count + 1
            elif prevnum == number:
                count = count + 1
            elif prevnum != number:
                keyvalueCountList.append([count , prevnum])
                prevnum = number
                count = 0
                count = count + 1
            else:
                continue
                
        if count > 0:
            keyvalueCountList.append([count , prevnum])
            
        keyvalueCountList.sort(key=lambda k: (k[0], k[1]), reverse=True)
        output = []
        
        for pair in (keyvalueCountList[0 : k]):
            output.append(pair[1])
        
        return output
                
                
            
        