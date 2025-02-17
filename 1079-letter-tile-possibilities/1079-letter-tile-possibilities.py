class Solution:
    def __init__(self):
        self.solution_set = set()
    
    def recursion(self, sequence, index, length, frequency_map):

        if index == length:
            non_empty_sequence = "".join(sequence)
            self.solution_set.add(non_empty_sequence)
            return
        
        for character in frequency_map:
            frequency_of_character = frequency_map[character]
            if frequency_of_character > 0:
                sequence[index] = character
                frequency_map[character] = frequency_map[character] - 1
                self.recursion(sequence, (index + 1), length, frequency_map)
                sequence[index] = None
                frequency_map[character] = frequency_map[character] + 1
        
        return
        
    def numTilePossibilities(self, tiles: str) -> int:
        size = 0
        distinct_characters_frequency = {}
        for character in tiles:
            if character not in distinct_characters_frequency:
                distinct_characters_frequency[character] = 0
            distinct_characters_frequency[character] = distinct_characters_frequency[character] + 1
            size = size + 1
        
        for length in range(2, (size + 1)):
            sequence = [None] * length
            for character in distinct_characters_frequency:
                sequence[0] = character
                distinct_characters_frequency[character] = distinct_characters_frequency[character] - 1
                self.recursion(sequence, 1, length, distinct_characters_frequency)
                distinct_characters_frequency[character] = distinct_characters_frequency[character] + 1
        
        # print(self.solution_set)
        # print(len(self.solution_set) , len(distinct_characters_frequency))
        solution_set_length = len(self.solution_set)
        one_length_sequences = len(distinct_characters_frequency)
        total_number_of_non_empty_sequences = solution_set_length + one_length_sequences
        return total_number_of_non_empty_sequences