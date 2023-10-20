class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        small_string = []
        big_string = []
        
        small_string_length = 0
        big_string_length = 0
        
        alen = len(a)
        blen = len(b)
        
        if alen > blen:
            small_string = list(b)
            big_string = list(a)
            
            small_string_length = blen
            big_string_length = alen
        else:
            small_string = list(a)
            big_string = list(b)
            
            small_string_length = alen
            big_string_length = blen
            
        print("small_string - ", small_string)
        print("big_string - ", big_string)
        print("small_string_length - ", small_string_length)
        print("big_string_length - ", big_string_length)
        
        binary_sum = ["0"] * (big_string_length + 1)
        print("binary_sum - ", binary_sum)
        binary_sum_pointer = big_string_length;
        
        small_position = small_string_length - 1
        big_position = big_string_length - 1
        carry = 0
        while small_position >= 0: 
            # 0 + 0 = 0 ; 0 + 1 = 1; 1 + 0 = 1; 1 + 1 = 10
            # carry = 0 ; then 1 + 1 = 10 ; 1 + 0 = 1; 0 + 1 = 1
            # carry = 1; then  0 + 1 = 10; 1 + 0 = 10; 1 + 1 = 11
            
            num1 = int(small_string[small_position])
            num2 = int(big_string[big_position])
            print ("num1 = ", num1, " and num2 = ", num2)
            
            if carry == 0:
                if num1 == 1 and num2 == 1:
                    carry = 1
                    binary_sum[binary_sum_pointer] = "0"
                    binary_sum_pointer = binary_sum_pointer - 1
                    print("step 1")
                elif num1 == 1 and num2 == 0:
                    carry = 0
                    binary_sum[binary_sum_pointer] = "1"
                    binary_sum_pointer = binary_sum_pointer - 1
                elif num1 == 0 and num2 == 1:
                    carry = 0
                    binary_sum[binary_sum_pointer] = "1"
                    binary_sum_pointer = binary_sum_pointer - 1
                elif num1 == 0 and num2 == 0:
                    carry = 0
                    binary_sum[binary_sum_pointer] = "0"
                    binary_sum_pointer = binary_sum_pointer - 1
            
            else:
                if carry == 1:
                    if num1 == 1 and num2 == 0:
                        carry = 1
                        binary_sum[binary_sum_pointer] = "0"
                        binary_sum_pointer = binary_sum_pointer - 1
                    elif num1 == 0 and num2 == 1:
                        carry = 1
                        binary_sum[binary_sum_pointer] = "0"
                        binary_sum_pointer = binary_sum_pointer - 1
                    elif num1 == 1 and num2 == 1:
                        carry = 1
                        binary_sum[binary_sum_pointer] = "1"
                        binary_sum_pointer = binary_sum_pointer - 1
                    elif num1 == 0 and num2 == 0:
                        carry = 0
                        binary_sum[binary_sum_pointer] = "1"
                        binary_sum_pointer = binary_sum_pointer - 1
            
            small_position = small_position - 1
            big_position = big_position - 1
        
        print("binary_sum - ", binary_sum)
        print("binary_sum_pointer - ", binary_sum_pointer)
        print("carry - ", carry)
        print("big_position - ", big_position)
        
        if big_position >= 0:
            while big_position >= 0:
                num1 = int(big_string[big_position])
                if carry == 1 and num1 == 1:
                    carry = 1
                    binary_sum[binary_sum_pointer] = "0"
                    binary_sum_pointer = binary_sum_pointer - 1
                elif carry == 1 and num1 == 0:
                    carry = 0
                    binary_sum[binary_sum_pointer] =  "1"
                    binary_sum_pointer = binary_sum_pointer - 1
                elif carry == 0 and num1 == 1:
                    carry = 0
                    binary_sum[binary_sum_pointer] =  "1"
                    binary_sum_pointer = binary_sum_pointer - 1
                elif carry == 0 and num1 == 0:
                    carry = 0
                    binary_sum[binary_sum_pointer] =  "0"
                    binary_sum_pointer = binary_sum_pointer - 1
                big_position = big_position - 1
        
        binary_sum[binary_sum_pointer] = str(carry)
        print("binary_sum - ", binary_sum)
        
        if binary_sum[0] == "0":
            return "".join(binary_sum[1:])
        
        return "".join(binary_sum)
