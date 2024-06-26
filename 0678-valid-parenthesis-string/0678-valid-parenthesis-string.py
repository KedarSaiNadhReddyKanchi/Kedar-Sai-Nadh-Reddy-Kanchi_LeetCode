class Solution:
    def checkValidString(self, s: str) -> bool:
        left_count = 0
        right_count = 0
        star_count = 0
        
        left_stack = []
        star_stack = []
        
        left_stack_size = 0
        star_stack_size = 0
        
        for position , symbol in enumerate(s):
            if symbol == "(":
                left_count = left_count + 1
                left_stack.append(position)
                left_stack_size = left_stack_size + 1
            elif symbol == "*":
                star_count = star_count + 1
                star_stack.append(position)
                star_stack_size = star_stack_size + 1
            else:
                if left_count > 0:
                    left_count = left_count - 1
                    left_stack.pop(-1)
                    left_stack_size = left_stack_size - 1
                elif star_count > 0:
                    star_count = star_count - 1
                    star_stack.pop(-1)
                    star_stack_size = star_stack_size - 1
                else:
                    return False
        
        if left_count == 0 and right_count == 0:
            return True
        
        left_stack_pointer = left_stack_size - 1
        star_stack_pointer = star_stack_size - 1
        while (left_stack_pointer >= 0 and star_stack_size > 0):
            leftValue = left_stack.pop(-1)
            starValue = star_stack.pop(-1)
            if leftValue < starValue:
                left_stack_pointer = left_stack_pointer - 1
                left_stack_size = left_stack_size - 1
                star_stack_size = star_stack_size - 1
                print(f"i reached here {left_stack_pointer}")
            else:
                break
        
        if left_stack_pointer >= 0:
            return False
        else:
            return True
        
        return False
        