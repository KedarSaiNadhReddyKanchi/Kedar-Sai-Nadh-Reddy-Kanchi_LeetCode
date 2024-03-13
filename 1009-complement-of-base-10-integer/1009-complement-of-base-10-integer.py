class Solution:
    def bitwiseComplement(self, n: int) -> int:
        
        if n == 0:
            return 1
        
        if n == 1:
            return 0
        
        binary = []
        normal = []
        count = 0
        while n > 0:
            remainder = n % 2
            normal.append(remainder)
            if remainder == 1:
                binary.append(0)
            else:
                binary.append(1) 
            n = (int)(n / 2)
            count = count + 1
        
        print(binary)
        print(normal)
        print(count)
        
        temp = 0
        newnumber = 0
        for bit in binary:
            value = 0
            if bit == 1:
                value = math.pow(2, temp)
            newnumber = newnumber + value
            temp = temp + 1
        
        return int(newnumber)
        