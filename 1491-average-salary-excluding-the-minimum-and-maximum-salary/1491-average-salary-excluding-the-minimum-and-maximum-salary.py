class Solution:
    def average(self, salary: List[int]) -> float:
        
        minimum = None
        highest = None
        total_salary = 0
        total_count = 0
        
        for amount in salary:
            if ((minimum is None) and (highest is None)): 
                minimum = amount 
                highest = amount
                total_salary = total_salary + amount
            else:
                if minimum > amount:
                    minimum = amount
                
                if highest < amount:
                    highest = amount
                
                total_salary = total_salary + amount
            total_count = total_count + 1
        
        net_salary = total_salary - minimum - highest
        net_count = total_count - 2
    
        return (net_salary / net_count)
        