class Solution:
    def __init__(self):
        self.original_array_0 = [0]
        self.original_array_1 = [1]

        self.original_array_flag_0 = True
        self.original_array_flag_1 = True

        self.n = None

    def getValueToBeAppended(self, last_value_in_the_array, bit_value_at_that_index):
        if bit_value_at_that_index == 1:
            if last_value_in_the_array == 1:
                return 0
            else:
                return 1
        else:
            return last_value_in_the_array

    def doesValidArrayExist(self, derived: List[int]) -> bool:
        original_array_0 = [0]
        original_array_1 = [1]

        original_array_flag_0 = True
        original_array_flag_1 = True

        n = len(derived)

        for position, xor_bit_value in enumerate(derived):

            # break out the loop when you reach the last bit
            if position == (n - 1):
                break

            # check if the flags for both the arrays are not false
            if (not original_array_flag_0) and (not original_array_flag_1):
                return False

            # build array with 0 as the starting bit
            if original_array_flag_0:
                last_value = original_array_0[-1]
                to_be_appended_value = self.getValueToBeAppended(last_value , xor_bit_value)
                original_array_0.append(to_be_appended_value)
            
            # build array with 1 as the starting bit
            if original_array_flag_1:
                last_value = original_array_1[-1]
                to_be_appended_value = self.getValueToBeAppended(last_value , xor_bit_value)
                original_array_1.append(to_be_appended_value)
        
        print(original_array_0)
        print()
        print(original_array_1)

        # check the last positions
        if original_array_flag_0:
            xor_bit_value = derived[-1]
            calculated_xor_value = original_array_0[0] ^ original_array_0[-1]
            if xor_bit_value == calculated_xor_value:
                return True
        
        if original_array_flag_1:
            xor_bit_value = derived[-1]
            calculated_xor_value = original_array_1[0] ^ original_array_1[-1]
            if xor_bit_value == calculated_xor_value:
                return True

        return False
