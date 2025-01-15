class Solution:
    def countBits(self, number):
        count = 0
        while number > 0:
            remainder = number % 2
            if remainder == 1:
                count = count + 1
            number = (int)(number / 2)
        return count

    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bits = self.countBits(num2)
        xor_minimum = max(num1 , num2)
        x = None

        number = 1
        end = num1 + num2

        while number <= end:
            number_set_bits = self.countBits(number)
            if number_set_bits == num2_set_bits:
                xor_value = number ^ num1
                if xor_value < xor_minimum:
                    x = number
                    xor_minimum = xor_value
            number = number + 1
        
        return x