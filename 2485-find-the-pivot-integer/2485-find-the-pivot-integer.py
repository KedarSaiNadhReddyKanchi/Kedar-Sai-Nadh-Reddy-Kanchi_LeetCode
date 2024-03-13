class Solution:
    def pivotInteger(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        leftsum = 1
        rightsum = (int)(((n) * (n + 1)) / 2)
        
        number = 2
        flag = False
        while number <= n:
            leftsum = leftsum + number
            rightsum = rightsum - (number - 1)
            if leftsum == rightsum:
                flag = True
                break
            else:
                number = number + 1
        
        if flag == True:
            return number
         
        return -1
            