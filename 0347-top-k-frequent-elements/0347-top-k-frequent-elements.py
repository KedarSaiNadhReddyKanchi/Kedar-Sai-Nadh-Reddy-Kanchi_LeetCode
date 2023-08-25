import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] = hashmap[num] + 1
        
    
        minheap = []
        heapq.heapify(minheap)
        
        for key in hashmap:
            heapq.heappush(minheap , [hashmap[key] , key] )
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        results = []
        
        while k > 0:
            value = heapq.heappop(minheap)
            results.append(value[1])
            k = k - 1
        
        return results
        
        
                
                
            
        