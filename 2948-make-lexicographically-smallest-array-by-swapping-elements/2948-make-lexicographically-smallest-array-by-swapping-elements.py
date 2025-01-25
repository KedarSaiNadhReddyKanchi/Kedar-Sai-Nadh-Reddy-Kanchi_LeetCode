class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:

        position_map = {}
        minheap = []
        heapq.heapify(minheap)
        result = [0] * len(nums)
        unoccupied_positions_map = {}

        for position, num in enumerate(nums):
            heapq.heappush(minheap, (num, position))
            position_map[position] = num
            unoccupied_positions_map[position] = True

        while len(minheap) > 0:
            popped_out_values = heapq.heappop(minheap)
            number, index = popped_out_values[0], popped_out_values[1]
            print(f"number = {number} index = {index} ")
            for unoccupied_index in unoccupied_positions_map:
                if unoccupied_positions_map[unoccupied_index]:
                    existing_number = position_map[unoccupied_index]
                    absolute_difference = abs(existing_number - number)
                    if absolute_difference <= limit:
                        position_map[unoccupied_index] = number
                        position_map[index] = existing_number
                        result[unoccupied_index] = number
                        unoccupied_positions_map[unoccupied_index] = False
                        # print(result)
                        # print(position_map)
                        # print()
                        break

        return result