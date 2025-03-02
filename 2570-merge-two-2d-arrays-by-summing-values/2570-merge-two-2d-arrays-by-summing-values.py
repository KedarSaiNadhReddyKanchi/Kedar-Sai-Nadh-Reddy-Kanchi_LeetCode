from sortedcontainers import SortedDict
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        ids = SortedDict()

        for id1 , value in nums1:
            ids[id1] = value
        
        for id2 , value in nums2:
            if id2 not in ids:
                ids[id2] = value
            else:
                ids[id2] = ids[id2] + value
        
        # print(ids)
        result = []
        for unique_id in ids:
            result.append([unique_id , ids[unique_id]])
        return result

