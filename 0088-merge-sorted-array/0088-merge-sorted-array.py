class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        pointer1 = m - 1
        pointer2 = n - 1
        writerpointer = m + n -1
        
        while writerpointer >= 0:
            if pointer1 >= 0 and pointer2 >= 0:
                value1 = nums1[pointer1]
                value2 = nums2[pointer2]
                if value1 >= value2:
                    nums1[writerpointer]  = value1
                    pointer1 = pointer1 - 1
                else:
                    nums1[writerpointer] = value2
                    pointer2 = pointer2 - 1
            elif pointer1 >= 0:
                nums1[writerpointer] = nums1[pointer1]
                pointer1 = pointer1 - 1
            else:
                nums1[writerpointer] = nums2[pointer2]
                pointer2 = pointer2 - 1
            
            writerpointer = writerpointer - 1
        
        