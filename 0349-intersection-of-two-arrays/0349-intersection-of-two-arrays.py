class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1_length = len(nums1)
        nums2_length = len(nums2)
        hashmap = {}
        output = {}
        
        if nums1_length < nums2_length:
            for num in nums1:
                if num not in hashmap:
                    hashmap[num] = 1
        else:
            for num in nums2:
                if num not in hashmap:
                    hashmap[num] = 1
        
        if nums1_length < nums2_length:
            for num in nums2:
                if num in hashmap:
                    if num not in output:
                        output[num] = 1
        else:
            for num in nums1:
                if num in hashmap:
                    if num not in output:
                        output[num] = 1
        
        result = []
        for key in output.keys():
            result.append(key)
            
        return result