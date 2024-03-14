class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == 1:
            return 0
        
        if num == 0:
            return 1
        
        reversed_binary_num = []
        complement = 0
        multiplier = 0
        
        while num > 0:
            remainder = num % 2
            num = (int)(num / 2)
            
            bit = None
            if remainder == 1:
                reversed_binary_num.append(0)
                bit = 0
            else:
                reversed_binary_num.append(1)
                bit = 1
            
            value = bit * math.pow(2, multiplier)
            complement = complement + value
            multiplier = multiplier + 1
            

        print(reversed_binary_num)
        print(complement)

        return (int)(complement)