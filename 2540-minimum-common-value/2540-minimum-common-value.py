class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums_1_index = 0
        nums_2_index = 0
        
        nums_1_length = len(nums1)
        nums_2_length = len(nums2)
        
        minimumvalue = None
        
        while ((nums_1_index < nums_1_length) and (nums_2_index < nums_2_length)):
            value1 = nums1[nums_1_index]
            value2 = nums2[nums_2_index]
            
            if value1 == value2:
                if minimumvalue == None:
                    minimumvalue = value1
                else:
                    if value1 < minimumvalue:
                        minimumvalue = value1
                
                nums_1_index = nums_1_index + 1
                nums_2_index = nums_2_index + 1
            
            else:
                if value1 < value2:
                    nums_1_index = nums_1_index + 1
                else:
                    nums_2_index = nums_2_index + 1
        
        if minimumvalue == None:
            return -1
        return minimumvalue