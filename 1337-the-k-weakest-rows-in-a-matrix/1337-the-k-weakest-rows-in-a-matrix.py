import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        reverseMinheap = []
        heapq.heapify(reverseMinheap)
        rowLength = len(mat[0])
        
        def binarySearch(row):
            # efficient way of finding the first position of 0 instead of performing linear search
            start = 0
            end = rowLength
            while start < end:
                mid = start + int((end - start) / 2)
                if row[mid] == 1:
                    start = mid + 1
                else:
                    end = mid
            return start
        
        for pos , row in enumerate(mat):
            position = binarySearch(row)
            soliders = position
            heapq.heappush(reverseMinheap , [(-1 * soliders) , (-1 * pos)])
            if len(reverseMinheap) > k:
                heapq.heappop(reverseMinheap)
            
        result = []
        while k > 0:
            popnum = heapq.heappop(reverseMinheap)
            result.append((-1 * popnum[1]))
            k = k - 1
        
        return result[::-1]
                