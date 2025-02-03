class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap = []
        heapq, heapify(maxheap)  # to store the maximum element of every window

        frequency_map = {}
        window = deque([])

        for position in range(k):
            current_value = nums[position]

            # add the element in to the window
            window.append(current_value)

            # add the element in to the frequency map or increment the count if already existing
            if current_value not in frequency_map:
                frequency_map[current_value] = 1
            else:
                frequency_map[current_value] = frequency_map[current_value] + 1
            
            # now also add the new element in to the max heap in order to maintain the maximum element in the window
            # i can add the element multiple times as it comes because i can have multiple instances of the same value
            heapq.heappush(maxheap, (-1 * current_value))

        max_sliding_window = []
        size = len(nums)

        # now iterating over the rest of the array
        for position in range(k, size):
            # get the maximum value in the window at this point - that is the window built upto this point
            maximum_element = -1 * maxheap[0]

            # add the maximum element to the max_sliding_window
            max_sliding_window.append(maximum_element)

            # now delete the element from the beginning of the window
            starting_element = window.popleft()

            # decrement the frequency of the deleted element from the frequency_map
            frequency_map[starting_element] = frequency_map[starting_element] - 1

            # delete the element from the frequency_map if the frequency of the deleted element becomes 0
            if frequency_map[starting_element] == 0:
                del frequency_map[starting_element]

            # check if the deleted element is the maximum element or not and if so delete the top element of the heap
            if starting_element == maximum_element:
                heapq.heappop(maxheap)

            # get the current value from the array now 
            current_value = nums[position]
            
            # add the element in to the window
            window.append(current_value)

            # add the element in to the frequency map or increment the count if already existing
            if current_value not in frequency_map:
                frequency_map[current_value] = 1
            else:
                frequency_map[current_value] = frequency_map[current_value] + 1
            
            # now also add the new element in to the max heap in order to maintain the maximum element in the window
            # i can add the element multiple times as it comes because i can have multiple instances of the same value
            heapq.heappush(maxheap, (-1 * current_value))
        
        # one final time get the maximum value of the lastly formed sliding window
        maximum_element = -1 * maxheap[0]

        # add the maximum element to the max_sliding_window
        max_sliding_window.append(maximum_element)

        return max_sliding_window