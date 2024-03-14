class Solution:
    def findComplement(self, num: int) -> int:
        
        if num == 1:
            return 0
        
        if num == 0:
            return 1
        
        binary_num = []
        
        while num > 0:
            remainder = num % 2
            binary_num.append(remainder)
            num = (int)(num / 2)
    
        print(binary_num)
        
        binary_num_length = len(binary_num)
        position = binary_num_length - 1
        while position >= 0:
            if binary_num[position] == 1:
                binary_num[position] = 0
            else:
                binary_num[position] = 1
            position = position - 1
        print(binary_num)
        
        complement = 0
        position = 0
        multiplier = 0
        position = binary_num_length - 1
        for bit in binary_num:
            value = bit * math.pow(2, multiplier)
            complement = complement + value
            multiplier = multiplier + 1
            print(complement)
        
        print()
        print(complement)
        return (int)(complement)