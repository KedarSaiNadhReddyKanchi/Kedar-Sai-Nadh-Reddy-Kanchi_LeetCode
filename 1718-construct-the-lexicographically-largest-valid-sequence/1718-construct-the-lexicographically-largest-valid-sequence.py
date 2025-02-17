class Solution:
    def __init__(self):
        self.sequence_length = 0
        self.n = 0
        self.solution = []
        self.visited = {}

    def recursion(self, sequence, helperhashmap, index):
        if index == self.sequence_length:
            self.solution.append(sequence)
            print(sequence)
            return True  # solution found
        
        value_at_index = sequence[index]
        if value_at_index is not None:
            result = self.recursion(sequence, helperhashmap, (index + 1))
            return True if result else False

        for value in range(self.n, 0, -1):
            # check if this number can be placed here or not
            if value not in helperhashmap:
                if value == 1:
                    helperhashmap[value] = {"previous_position": index, "occurence_count": 1}
                    sequence[index] = value
                    result = self.recursion(sequence, helperhashmap, (index + 1))
                    if result:
                        return True
                    sequence[index] = None
                    del helperhashmap[value]
                else:
                    current_position = index
                    second_position = index + value
                    if second_position >= self.sequence_length:
                        continue

                    if sequence[second_position] is not None:
                        continue

                    helperhashmap[value] = {"previous_position": second_position, "occurence_count": 2}
                    sequence[index] = value
                    sequence[second_position] = value

                    result = self.recursion(sequence, helperhashmap, (index + 1))
                    if result:
                        return True

                    sequence[index] = None
                    sequence[second_position] = None
                    del helperhashmap[value]
        
        return False

    def constructDistancedSequence(self, n: int) -> List[int]:
        if n == 1:
            return [1]

        self.sequence_length = 1 + ((n - 2 + 1) * 2)
        sequence = [None] * self.sequence_length
        sequence[0] = n
        sequence[n] = n
        self.n = n
        helperhashmap = {}
        helperhashmap[n] = {"previous_position": n, "occurence_count": 2}
        self.recursion(sequence, helperhashmap, 1)
        print(self.solution)
        return self.solution[0]
