class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        
        cost_length = len(cost)
        
        if cost_length == 2:
            value1 = cost[0]
            value2 = cost[1]
            if value1 <= value2:
                return value1
            else:
                return value2
        
        if cost_length == 1:
            return 0
                
        topcost = 0
        finalstepcost = cost[-1] # will out the last element in the list
        cost.append(0)
        
        idx = (cost_length + 1) - 3
        minimumCost = None
        
        while idx >= 0:
            value1 = cost[idx] + finalstepcost
            value2 = cost[idx] + topcost
            
            topcost = finalstepcost
            
            if value1 <= value2:
                finalstepcost = value1
            else:
                finalstepcost = value2
            
            if idx == 1 or idx == 0:
                if minimumCost == None:
                    minimumCost = finalstepcost
                else:
                    if finalstepcost < minimumCost:
                        minimumCost = finalstepcost
            idx = idx - 1
        
        # print(minimumCost)
        return minimumCost
            
                
                
                
        
        