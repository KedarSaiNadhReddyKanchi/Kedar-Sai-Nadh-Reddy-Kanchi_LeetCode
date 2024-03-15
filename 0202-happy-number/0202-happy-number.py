class Solution:
    def isHappy(self, n: int) -> bool:
        
        if n == 1:
            return True
        
        new_value = 0 
        upper_limit = math.pow(2, 31)
        first_iteration = True
        flag = False
        iteration_count = 0
        
        while ((new_value < upper_limit)):
            temp = None
            if first_iteration:
                temp = n
                first_iteration = False
            else:
                temp = new_value
            
            total = 0
            while temp > 0:
                remainder = temp % 10
                total = total + (remainder * remainder)
                temp = (int)(temp / 10)
            
            new_value = total
            if new_value == 1:
                flag = True
                break
            
            iteration_count = iteration_count + 1
            if iteration_count > 100:
                break
                
            if new_value == n:
                break
        
        return flag
                
        