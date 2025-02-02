class Solution:
    def findValidPair(self, s: str) -> str:
        frequency_map = {}
        for digit in s:
            if digit not in frequency_map:
                frequency_map[digit] = 0
            frequency_map[digit] = frequency_map[digit] + 1

        pair = deque([])
        for digit in s:
            if len(pair) < 2:
                pair.append(digit)
            
            if len(pair) == 2:
                first_digit = pair[0]
                first_digit_frequency = frequency_map[first_digit]
                
                second_digit = pair[1]
                second_digit_frequency = frequency_map[second_digit]

                condition_1 = int(first_digit) != int(second_digit)
                condition_2 = int(first_digit) == first_digit_frequency
                condition_3 = int(second_digit) == second_digit_frequency

                if condition_1 and condition_2 and condition_3:
                    return ("" + str(first_digit) + "" + str(second_digit))
                
                pair.popleft()
        
        return ""


                

