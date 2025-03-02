class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pointer_1 = 0
        pointer_2 = 0

        nums1_size = len(nums1)
        nums2_size = len(nums2)

        result = []

        while (pointer_1 < nums1_size) and (pointer_2 < nums2_size):
            id_at_pointer_1 , value_1 = nums1[pointer_1]
            id_at_pointer_2 , value_2 = nums2[pointer_2]
            if id_at_pointer_1 == id_at_pointer_2:
                ids_sum = value_1 + value_2
                result.append([id_at_pointer_1 , ids_sum])
                pointer_1 = pointer_1 + 1
                pointer_2 = pointer_2 + 1
            else:
                if id_at_pointer_1 < id_at_pointer_2:
                    result.append([id_at_pointer_1 , value_1])
                    pointer_1 = pointer_1 + 1
                else:
                    result.append([id_at_pointer_2 , value_2])
                    pointer_2 = pointer_2 + 1
        
        while (pointer_1 >= nums1_size) and (pointer_2 < nums2_size):
            id_at_pointer_2 , value_2 = nums2[pointer_2]
            result.append([id_at_pointer_2 , value_2])
            pointer_2 = pointer_2 + 1
        
        while (pointer_2 >= nums2_size) and (pointer_1 < nums1_size):
            id_at_pointer_1 , value_1 = nums1[pointer_1]
            result.append([id_at_pointer_1 , value_1])
            pointer_1 = pointer_1 + 1
        
        print(nums1_size , nums2_size, pointer_1, pointer_2)
        return result
