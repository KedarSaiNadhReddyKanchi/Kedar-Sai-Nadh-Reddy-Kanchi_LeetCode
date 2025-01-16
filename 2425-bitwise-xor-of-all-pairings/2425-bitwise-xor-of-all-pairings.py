class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # brute force
        result = 0
        for num1 in nums1:
            for num2 in nums2:
                result = result ^ (num1 ^ num2)
        
        return result