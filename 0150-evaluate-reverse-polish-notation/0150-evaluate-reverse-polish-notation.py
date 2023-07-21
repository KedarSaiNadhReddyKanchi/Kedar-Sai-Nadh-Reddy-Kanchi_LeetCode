class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # initialize a stack
        valuestack = []
        operands = {
            '+': 1,
            '-': 1,
            '*': 1,
            '/': 1,
        }
        
        for token in tokens:
            
            if token in operands:
                current_length = len(valuestack)
                second_charcter = valuestack.pop()
                first_character = valuestack.pop()
            
                if token == '+':
                    new_value = first_character + second_charcter
                    
                elif token == '-':  
                    new_value = first_character - second_charcter
                elif token == '*':
                    new_value = first_character * second_charcter
                elif token == '/':
                    new_value = int(first_character / second_charcter)
                    
                valuestack.append(new_value)
            
            else:
                valuestack.append(int(token))
        
        print(valuestack)
        return valuestack[0]