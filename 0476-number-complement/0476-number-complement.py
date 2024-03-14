class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == 1:
            return 0
        
        if num == 0:
            return 1
        
        reversed_binary_num = []
        
        while num > 0:
            remainder = num % 2
            num = (int)(num / 2)
            
            if remainder == 1:
                reversed_binary_num.append(0)
            else:
                reversed_binary_num.append(1)

        complement = 0
        multiplier = 0

        for bit in reversed_binary_num:
            value = bit * math.pow(2, multiplier)
            complement = complement + value
            multiplier = multiplier + 1

        return (int)(complement)