import math 
class Solution:
    
    def calculateEuclideanDistance(self , point):
        xcor , ycor = point
        return math.sqrt(((xcor * xcor) + (ycor * ycor)))
    
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        hashmap = {}
        
        for point in points:
            distance = self.calculateEuclideanDistance(point)
            if distance not in hashmap:
                hashmap[distance] = []
            hashmap[distance].append(point)
        # hashmap[3.1622776601683795].append([2,3])
        
        keysList = [key for key in hashmap]
        keysList.sort()
        results = []
        count = 0
        print(keysList)
        for key in keysList:
            for point in hashmap[key]:
                results.append(point)
                count = count + 1
                if count == k:
                    break
            if count == k:
                    break
        print(results)
        return results
            
        
        
        