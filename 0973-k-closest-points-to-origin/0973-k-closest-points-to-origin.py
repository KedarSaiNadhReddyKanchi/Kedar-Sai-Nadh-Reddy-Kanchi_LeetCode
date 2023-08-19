import heapq
class Solution:
    
    def calculateEuclideanDistance(self , point):
        xcor , ycor = point
        return math.sqrt(((xcor * xcor) + (ycor * ycor)))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # APPROACH USING HEAPS
        minheap = []
        heapq.heapify(minheap)
        
        for point in points:
            distanceFromOrigin = self.calculateEuclideanDistance(point)
            heapq.heappush(minheap , [distanceFromOrigin , point])
        
        result = []
        # print(minheap)
        while k > 0:
            result.append(heapq.heappop(minheap)[1])
            k = k - 1
        
        return result
            

        # ONE APPROACH BEFORE I LEARNED HEAPS
#         N = len(points)
#         dists = []
#         for point in points:
#             dists.append(self.calculateEuclideanDistance(point))
            
#         dists.sort()
#         print(dists)
#         distK = dists[k-1];
#         print(distK)
        
#         ans = []
#         for point in points:
#             if self.calculateEuclideanDistance(point) <= distK:
#                 ans.append(point)
        
#         return ans

            