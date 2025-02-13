class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # define a min heap
        minheap = []
        heapq.heapify(minheap)

        # now run a loop to store all those value in the minheap
        for num in nums:
            heapq.heappush(minheap , num)
        
        # now since I have the minheap
            # what I want to do is that I would like to loop over the heap
                # until all the values are greater than or equal to k
                # or if the number of values in the heap fall below 2
            # and since it is given in the constraint that an answer is for present 
                # i do not need to worry about the heap size falling below 1 element i.e. becoming empty
        
        number_of_operations = 0

        top_element = minheap[0]
        while top_element < k:

            first_smallest_number = heapq.heappop(minheap)
            second_smallest_number = heapq.heappop(minheap)

            first_operation_value = min(first_smallest_number , second_smallest_number) * 2
            second_operation_value = max(first_smallest_number , second_smallest_number)
            
            combined_operations_value = first_operation_value + second_operation_value

            heapq.heappush(minheap , combined_operations_value)
            number_of_operations = number_of_operations + 1
            top_element = minheap[0]
        
        return number_of_operations
            