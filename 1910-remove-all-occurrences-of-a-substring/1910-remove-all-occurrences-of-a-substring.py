class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        size = len(s)
        part_string_size = len(part)

        final_string_stack = []
        final_string_size = 0

        for character in s:
            final_string_stack.append(character)
            final_string_size = final_string_size + 1
            if final_string_size >= part_string_size:
                starting_point = final_string_size - part_string_size
                final_string = "".join(final_string_stack[starting_point : ])
                if final_string == part:
                    count = part_string_size
                    while count > 0:
                        final_string_stack.pop()
                        count = count - 1
                        final_string_size = final_string_size - 1
        
        final_string = "".join(final_string_stack)
        return final_string


