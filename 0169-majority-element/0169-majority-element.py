class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        total_count = 0
        hashmap = {}
        
        high_number = None
        high_count = None
        
        for num in nums:
            if num in hashmap:
                hashmap[num] = hashmap[num] + 1
            else:
                hashmap[num] = 1
                
            if ((high_number is None) and (high_count is None)):
                high_number = num
                high_count = hashmap[num]
            else:
                if hashmap[num] > high_count:
                    high_number = num
                    high_count = hashmap[num]
            
            total_count = total_count + 1
            
        limit = int(total_count / 2)
        # print("total count is = ", total_count)
        # print("high_number = ", high_number)
        # print("high_count is = ", high_count)
        # print(hashmap)
        if high_count > limit:
            return high_number
                
        return 0
                
            
        