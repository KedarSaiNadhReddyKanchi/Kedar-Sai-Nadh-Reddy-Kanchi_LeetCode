import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # for this problem implement max heap
        # after the max heap is implemented
            # start by popping two elements at once - which gives us the heaviest two stones
            # then after we execute the give algorithm and left with a weight - push it back into the max heap
            
        if len(stones) == 1:
            return stones[0]
        
        if len(stones) == 2:
            a = stones[0]
            b = stones[1]
            if a == b:
                return 0
            elif a > b:
                return a - b
            else:
                return b - a
            
        maxheap = []
        heapq.heapify(maxheap)
        
        # creates a max heap but as a min heap since each value is mutliplied by -1
        for stoneweight in stones:
            heapq.heappush(maxheap , (-1 * stoneweight))
         
        
        while len(maxheap) >= 2:
            first_highest_element = -1 * heapq.heappop(maxheap)
            second_highest_element = -1 * heapq.heappop(maxheap)
            
            if first_highest_element == second_highest_element:
                continue
            else:
                remaining_weight = first_highest_element - second_highest_element
                heapq.heappush(maxheap , (-1 * remaining_weight))
        
        if len(maxheap) > 0:
            return (-1 *  maxheap[0])
        
        return 0
        