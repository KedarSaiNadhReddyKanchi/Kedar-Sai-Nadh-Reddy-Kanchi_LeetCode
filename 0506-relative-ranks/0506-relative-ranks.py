import heapq
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        highHeap = []
        heapq.heapify(highHeap)
        
        for num in score:
            heapq.heappush(highHeap , (-1 * num))
            
        hashmap = {}
        gold = "Gold"
        silver = 'Silver'
        bronze = "Bronze"
        count = 0
        
        while len(highHeap) > 0:
            popped_value = heapq.heappop(highHeap) * -1
            count = count + 1
            if gold not in hashmap:
                hashmap[popped_value] = "Gold Medal"
                hashmap[gold] = popped_value
            elif silver not in hashmap:
                hashmap[popped_value] = "Silver Medal"
                hashmap[silver] = popped_value
            elif bronze not in hashmap:
                hashmap[popped_value] = "Bronze Medal"
                hashmap[bronze] = popped_value
            else:
                hashmap[popped_value] = count
        
        answer = []
        for num in score:
            if num in hashmap:
                answer.append(str(hashmap[num]))
        return answer