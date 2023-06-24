class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        hash_map = {
            '(': 0,
            '{': 0,
            '[': 0,
        }
        
        strlist = list(s)
        flag = True
        
        stack = []
        
        for character in strlist:
            if character == '(':
                stack.append(character)
            elif character == '{':
                stack.append(character)
            elif character == '[':
                stack.append(character)
            
            elif character == ')':
                if len(stack) > 0:
                    topchar = stack.pop()
                    if topchar == '(':
                        continue
                    else:
                        stack.append(topchar)
                        flag = False
                        break
                else:
                    stack.append(')')
                    flag = False
                    break
            
            elif character == '}':
                if len(stack) > 0:
                    topchar = stack.pop()
                    if topchar == '{':
                        continue
                    else:
                        stack.append(topchar)
                        flag = False
                        break
                else:
                    stack.append('}')
                    flag = False
                    break
            
            elif character == ']':
                if len(stack) > 0:
                    topchar = stack.pop()
                    if topchar == '[':
                        continue
                    else:
                        stack.append(topchar)
                        flag = False
                        break
                else:
                    stack.append(']')
                    flag = False
                    break

        if len(stack) == 0:
            return True
        elif len(stack) > 0:
            return False
        
        return flag