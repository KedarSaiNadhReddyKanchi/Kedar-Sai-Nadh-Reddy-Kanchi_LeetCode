import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        # understanding from the solution given in the article
        
        # retrieve the length of the matrix as the question says that the provided input is a n x n matrix
        N = len(matrix)
        
        # initialise a minHeap to store the elements
        minHeap = []
        heapq.heapify(minHeap)
        
        # now it is given that the lists in the input matrix are sorted rowWise and columnWise
        # so now we need to find the minimum of (N , k)
            # this is because, let's assume that the input matrix has 100 rows and we need to find the 5th smallest
            # so in that case the highest row that we need to reach would be the 5th row and ignore the lower portion
        lastRowRequiredToReach = min(N , k)
        
        # so now once we have the value for the lastRowRequiredToReach
        # we will iterate over the 1st column from the 1st row till the lastRowRequiredToReach row
        
        for index in range(lastRowRequiredToReach):
            # we will add 3 values as a triplet to the minHeap
            # valuesToAppend = [matrix[rowNumber][columnNumber] , rowNumber , columnNumber]
                # but in this case we are iterating only over the 1st column from the 1st row till the min(N,k) row 
                # so the columnNumber = 0 and the rowNumber = index
                # therefore the syntax to follow is valuesToAppend = [matrix[index][0] , index , 0]
            valuesToAppend = [matrix[index][0] , index , 0]
            heapq.heappush(minHeap , valuesToAppend)
            
        # now we will iterate until we find the kth smallest element
        # for that we will implement a while loop until k > 0
        
        lastPoppedSmallestElement = None
        while k > 0:
            # first retrieve the smallest element from the formed minHeap
            poppedValue = heapq.heappop(minHeap)
            lastPoppedSmallestElement , rowNumber , columnNumber = poppedValue[0] , poppedValue[1] , poppedValue[2]
            
            # now we check if the columnNumber of the popped element is less than N - 1
                # because if so we need to add the next element from the same row popped but from the next column
            if columnNumber < (N - 1):
                valuesToAppend = [matrix[rowNumber][(columnNumber + 1)] , rowNumber , (columnNumber + 1)]
                heapq.heappush(minHeap , valuesToAppend)
            
            # finally decrement the value of k by 1
                # because we popped out one smallest element 
            k = k - 1
        
        return lastPoppedSmallestElement
        
        
        
        
        