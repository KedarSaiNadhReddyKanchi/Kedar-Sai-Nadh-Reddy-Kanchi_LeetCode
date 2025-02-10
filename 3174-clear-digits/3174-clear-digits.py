class Solution:
    def clearDigits(self, s: str) -> str:
        # as per the constraint the input is in a format where it is possible to delete all the digits
        # so I would like to use an additional stack
        final_string_stack = []
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for character in s:
            if character in digits:
                final_string_stack.pop()
            else:
                final_string_stack.append(character)
        
        final_string_result = "".join(final_string_stack)
        return final_string_result

