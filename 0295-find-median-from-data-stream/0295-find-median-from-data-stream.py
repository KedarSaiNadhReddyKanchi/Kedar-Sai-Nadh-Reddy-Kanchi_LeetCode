import heapq
class MedianFinder:

    def __init__(self):
        # to store the larger half of the numbers
        self.minheap = []
        heapq.heapify(self.minheap)
        
        # to store the smaller half of the numbers
        self.maxheap = []
        heapq.heapify(self.maxheap)
        
        self.runningMedian = None
        
        

    def addNum(self, num: int) -> None:
        
        # as per viewed solution
        
        if len(self.minheap) == 0 and len(self.maxheap) == 0:
            # step 1 - add the new number to the maxheap
            heapq.heappush(self.maxheap , (-1 * num))
            self.runningMedian = num
        else:
            # step 1 - add the new number to the maxheap
            heapq.heappush(self.maxheap , (-1 * num))
            
            # step 2 : now since a new element is added to the maxheap
            # we need to remove the highest element from the maxheap and then add it to the min heap
            popnum = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap , (-1 * popnum))
            
            # step 3: we need to make sure that the length of the minheap is less than/equal to that of the maxheap
            # so after step 2 , the minheap might contain more elements than maxheap
            # so we need to pop the top element from the min heap and push it to the maxheap
            if len(self.minheap) > len(self.maxheap):
                popnum = heapq.heappop(self.minheap)
                heapq.heappush(self.maxheap , (-1 * popnum))
                
#         print("self.minheap = ", self.minheap)
#         print("self.maxheap = " , self.maxheap)
        

    def findMedian(self) -> float:
        if len(self.maxheap) > len(self.minheap):
            return (-1 * self.maxheap[0])
        else:
            return ((-1 * self.maxheap[0]) + self.minheap[0]) / 2
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()