class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
#         if m == 0:
#             for position , num in enumerate(nums2):
#                 nums1[position] = num
#             current_length = len(nums1)
#             position = current_length - 1
#             while position > n:
#                 del nums1[position]
        
#         if n == 0:
#             position = len(nums1) - 1
#             while position > m:
#                 del nums1[position]
        
        position1 = 0
        position2 = 0
        insertion_point = 0
        
        numscopy = nums1[0 : m]
        
        while position1 < m and position2 < n:
            value1 = numscopy[position1]
            value2 = nums2[position2]
            if value1 <= value2 :
                position1 = position1 + 1
                nums1[insertion_point] = value1
                insertion_point = insertion_point + 1
            else:
                nums1[insertion_point] = value2
                position2 = position2 + 1
                insertion_point = insertion_point + 1
        
        if position1 < m and position2 >= n:
            while position1 < m:
                nums1[insertion_point] = numscopy[position1]
                position1 = position1 + 1
                insertion_point = insertion_point + 1
        
        if position1 >= m and position2 < n:
            while position2 < n:
                nums1[insertion_point] = nums2[position2]
                position2 = position2 + 1
                insertion_point = insertion_point + 1
                
        
        
        