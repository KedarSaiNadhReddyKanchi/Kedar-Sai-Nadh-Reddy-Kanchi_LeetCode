import heapq

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        maxHeap = []
        heapq.heapify(maxHeap)
        
        for num in nums:
            heapq.heappush(maxHeap , (-1 * num))
        
        popNum = None
        
        while k > 0:    
            popNum = heapq.heappop(maxHeap)
            k = k - 1
            
        return (-1 * popNum)
        
        