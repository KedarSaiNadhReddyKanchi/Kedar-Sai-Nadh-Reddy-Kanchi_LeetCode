class NumberContainers:

    def __init__(self):
        # i would like to deine a hashmap to store the numbers 
        self.numbers_container = {}

        # I would like to deine another hashmap to store the indices for the numbers inserted
        self.index_mapping = {}
        
    def change(self, index: int, number: int) -> None:
        
        # first I need to check if the given index is present in the numbers container or not 
        is_index_present = False

        # also If the index is existing then I need to get the current value at that index
        current_existing_value_at_index = None
        
        if index in self.numbers_container:
            is_index_present = True
            current_existing_value_at_index = self.numbers_container[index]
        
        # now either update the existing index with the new value or create a new entry
        self.numbers_container[index] = number

        # let's say I am updating the index with the same existing value
        # then I would not like to push the same index again into the number's memory heap
        # there if the index was previsouly existing and the previsouly existing value is same the new value
        # then I will not push the same index again into the number's memory heap
        if is_index_present and (current_existing_value_at_index == number):
            return

        # now I need to add the index to the number's list of indices
        if number not in self.index_mapping:
            self.index_mapping[number] = []

        # Add index to the min heap for this number
        heapq.heappush(self.index_mapping[number], index)

    def find(self, number: int) -> int:
        # if the number is not in the index mapping then return -1
        if number not in self.index_mapping:
            return -1

        # Keep checking top element until we find valid index
        while self.index_mapping[number]:
            # get the minimum element from the heap
            minimum_index = self.index_mapping[number][0]

            # get the number present at the retrieved minimum index
            number_present_at_the_retrived_minimum_index = self.numbers_container[minimum_index]

            # check if the number in question and the number present at the minimum index are the same or not
            # if so then return it
            if number == number_present_at_the_retrived_minimum_index:
                return minimum_index
            
            # or else pop the index from the number's memory map
            heapq.heappop(self.index_mapping[number])
        
        return -1

                
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)