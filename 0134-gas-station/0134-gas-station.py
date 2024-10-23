class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        # if sum of gas is less than sum of cost then you cannot make a circle so return -1
        gas_sum = sum(gas)
        cost_sum = sum(cost)
        if gas_sum < cost_sum:
            return -1
        
        start = 0
        stay = 0
        gas_length = len(gas)
        cost_length = gas_length
        
        gas_in_car = 0
        
        while (start < gas_length):
            gas_available = gas[start]
            travel_cost = cost[start]
            
            gas_in_car = gas_in_car + gas_available
            gas_in_car = gas_in_car - travel_cost
            
            if gas_in_car < 0:
                gas_in_car = 0
                stay = start + 1
                
            start = start + 1
                

            
        return stay
                
        