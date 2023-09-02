class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if n == 0:
            position = len(nums1) - 1
            while position >= m:
                del nums1[position]
                position = position - 1
        
        if m == 0:
            position = len(nums2) - 1
            while position >= 0:
                nums1.insert(0 , nums2[position])
                position = position - 1
            print(nums1)
                
            position = len(nums1) - 1
            while position >= m:
                del nums1[position]
                position = position - 1
        
        nums1_pointer1 = 0
        nums2_pointer2 = 0
        
        nums1_modified_length = m
        # nums1_sliced = nums1[0 : m]
        # print(nums1_sliced)
        # nums1 = nums1_sliced
        pivot_point = m
        
        while ((nums1_pointer1 < (m + n)) and (nums2_pointer2 < n) and (nums1_pointer1 < nums1_modified_length) ):
            nums1_value1 = nums1[nums1_pointer1]
            nums2_value2 = nums2[nums2_pointer2]
            
            if nums1_value1 > nums2_value2:
                nums1.insert(nums1_pointer1 , nums2_value2)
                nums2_pointer2 = nums2_pointer2 + 1
                nums1_modified_length = nums1_modified_length +  1
                pivot_point = pivot_point + 1
                nums1_pointer1 = nums1_pointer1 + 1
                if nums1_pointer1 >= pivot_point:
                    break
            else:
                nums1_pointer1 = nums1_pointer1 + 1
                if nums1_pointer1 >= pivot_point:
                    break
                
        
        if nums2_pointer2 < n:
            while nums2_pointer2 < n:
                nums1.insert(nums1_pointer1 , nums2[nums2_pointer2])
                nums2_pointer2 = nums2_pointer2 + 1
                nums1_pointer1 = nums1_pointer1 + 1
        
        position = len(nums1) - 1
        while position >= (m + n):
            del nums1[position]
            position = position - 1
            

                
        