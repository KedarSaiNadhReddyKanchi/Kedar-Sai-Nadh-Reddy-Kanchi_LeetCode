import heapq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        if ((ladders == 0) and (bricks == 0)):
            if len(heights) > 1:
                nextBuildingHeight = heights[1]
                if heights[0] >= nextBuildingHeight:
                    return 1
                else:
                    return 0
            else:
                return 0
        
        if ((ladders == 0) or (bricks == 0)):
            lastPositionReached = 0
            for index , currentBuildingHeight in enumerate(heights):
                if index > 0:
                    prevBuildingHeight = heights[index - 1]
                    if currentBuildingHeight > prevBuildingHeight:
                        difference = currentBuildingHeight - prevBuildingHeight
                        if ladders == 0:
                            if bricks >= difference:
                                bricks = bricks - difference
                                lastPositionReached = index
                            else:
                                break
                        elif bricks == 0:
                            if ladders > 0:
                                ladders = ladders - 1
                                lastPositionReached = index
                            else:
                                break
                    else:
                        lastPositionReached = index
                else:
                    lastPositionReached = index
            
            return lastPositionReached
        
        else:
            minHeap = []
            heapq.heapify(minHeap)
            lastPositionReached = 0
            
            for index , currentBuildingHeight in enumerate(heights):
                if index > 0:
                    prevBuildingHeight = heights[index - 1]
                    if currentBuildingHeight > prevBuildingHeight:
                        difference = currentBuildingHeight - prevBuildingHeight
                        if ladders > 0:
                            heapq.heappush(minHeap , difference)
                            ladders = ladders - 1
                            lastPositionReached = index
                        else:
                            leastClimbForLadder = minHeap[0]
                            if leastClimbForLadder < difference:
                                if bricks >= leastClimbForLadder:
                                    bricks = bricks - leastClimbForLadder
                                    heapq.heappop(minHeap)
                                    heapq.heappush(minHeap , difference)
                                    lastPositionReached = index
                                else:
                                    break
                            else:
                                if bricks >= difference:
                                    bricks = bricks - difference
                                    lastPositionReached = index
                                else:
                                    break
                    else:
                        lastPositionReached = index
                else:
                    lastPositionReached = index
                    
            return lastPositionReached
        
        return 0
                        
                    
            
            
            
            
            
                    
        