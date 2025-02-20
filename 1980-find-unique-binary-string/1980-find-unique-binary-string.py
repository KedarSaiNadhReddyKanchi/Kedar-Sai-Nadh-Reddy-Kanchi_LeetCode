class Solution:
    def binaryToNumber(self, binaryString, n):
        decimal_number = 0
        power = n - 1
        for bit in binaryString:
            if bit == "1":
                value = (2 ** power)
                decimal_number = decimal_number + value
            power = power - 1
        return decimal_number
    
    def decimalToBinary(self, decimal_number, n):
        binary_string= ["0"] * n
        index = n - 1
        while decimal_number > 0:
            remainder = decimal_number % 2
            if remainder == 1:
                binary_string[index] = "1"
            decimal_number = int(decimal_number / 2)
            index = index - 1
        return "".join(binary_string)

    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums.sort()
        previous_decimal_number = -1
        for binaryString in nums:
            decimal_number = self.binaryToNumber(binaryString , n)
            difference = decimal_number - previous_decimal_number
            # print(binaryString, decimal_number, previous_decimal_number, difference)
            if difference == 1:
                previous_decimal_number = decimal_number
            else:
                expected_decimal_number = previous_decimal_number + 1
                missing_binary_string = self.decimalToBinary(expected_decimal_number , n)
                return missing_binary_string
        
        # if at this point then everything is order so check for the next element
        expected_decimal_number = previous_decimal_number + 1
        missing_binary_string = self.decimalToBinary(expected_decimal_number , n)
        return missing_binary_string