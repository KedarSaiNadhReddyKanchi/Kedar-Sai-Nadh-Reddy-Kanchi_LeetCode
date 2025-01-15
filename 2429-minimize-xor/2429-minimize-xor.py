class Solution:
    def countBits(self, number):
        result = deque([])
        count = 0
        while number > 0:
            remainder = number % 2
            if remainder == 1:
                count = count + 1
            result.appendleft(remainder)
            number = (int)(number / 2)
        return [count , result]
    
    def formNumberFromTheBitRepresentation(self, bit_array, size):
        power = size - 1
        pointer = 0
        formed_number = 0
        while pointer < size:
            bit_value = (2 ** power) * bit_array[pointer]
            formed_number = formed_number + bit_value
            pointer = pointer + 1
            power = power - 1
        return formed_number

    def minimizeXor(self, num1: int, num2: int) -> int:
        num2_set_bits_count , num2_bit_representation = self.countBits(num2)
        num2_bit_representation_size = len(num2_bit_representation)
        
        print(num2_set_bits_count)
        print(num2_bit_representation)
        print(num2_bit_representation_size)

        num1_set_bits_count , num1_bit_representation = self.countBits(num1)
        num1_bit_representation_size = len(num1_bit_representation)

        if num1_bit_representation_size < num2_bit_representation_size:
            difference = num2_bit_representation_size - num1_bit_representation_size
            while difference > 0:
                num1_bit_representation.appendleft(0)
                difference = difference - 1
        
        num1_bit_representation_size = len(num1_bit_representation)
        
        print(num1_set_bits_count)
        print(num1_bit_representation)
        print(num1_bit_representation_size)

        if num1_set_bits_count == num2_set_bits_count:
            return num1
        
        if num1_set_bits_count < num2_set_bits_count:
            difference = num2_set_bits_count - num1_set_bits_count
            pointer = num1_bit_representation_size - 1
            while pointer >= 0 and difference > 0:
                if num1_bit_representation[pointer] == 0:
                    num1_bit_representation[pointer] = 1
                    difference = difference - 1
                pointer = pointer - 1
            print(f"new num1_bit_representation = {num1_bit_representation}")
            formed_number = self.formNumberFromTheBitRepresentation(num1_bit_representation, num1_bit_representation_size)
            return formed_number

        if num1_set_bits_count > num2_set_bits_count:
            difference = num1_set_bits_count - num2_set_bits_count
            pointer = num1_bit_representation_size - 1
            while pointer >= 0 and difference > 0:
                if num1_bit_representation[pointer] == 1:
                    num1_bit_representation[pointer] = 0
                    difference = difference - 1
                pointer = pointer - 1
            
            formed_number = self.formNumberFromTheBitRepresentation(num1_bit_representation, num1_bit_representation_size)
            return formed_number