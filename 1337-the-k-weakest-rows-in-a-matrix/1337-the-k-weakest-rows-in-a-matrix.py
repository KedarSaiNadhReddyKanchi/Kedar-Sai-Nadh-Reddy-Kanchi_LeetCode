import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        minheap = []
        heapq.heapify(minheap)
        
        for pos , row in enumerate(mat):
            try:
                position = row.index(0)
                soliders = position
                heapq.heappush(minheap , [soliders , pos])
            except:
                soliders = len(row)
                heapq.heappush(minheap , [soliders , pos])
            
        result = []
        while k > 0:
            popnum = heapq.heappop(minheap)
            result.append(popnum[1])
            k = k - 1
        
        return result
                