class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        part_string_map = {position : character for position , character in enumerate(part)}
        part_string_size = len(part_string_map)
        build_string = []
        build_string_index = 0
        buid_string_size = 0
        size = len(s)
        position = 0
        final_string = []

        for character in s:
            pointing_character = part_string_map[build_string_index]
            if character == pointing_character:
                build_string.append(character)
                buid_string_size = buid_string_size + 1
                build_string_index = build_string_index + 1
                if buid_string_size == part_string_size:
                    build_string = []
                    build_string_index = 0
                    buid_string_size = 0

                    # now check the last character from the final string 
                    # if it is matching the first character of the part string 
                    # remove it from there and add it to the build string so that from the next character
                    # onwards it would be built sequentially as intended
                    if len(final_string) > 0:
                        last_inserted_character = final_string[-1]
                        temp_pointing_character = part_string_map[build_string_index]
                        if last_inserted_character == temp_pointing_character:
                            final_string.pop()
                            build_string.append(temp_pointing_character)
                            buid_string_size = buid_string_size + 1
                            build_string_index = build_string_index + 1
            else:
                # check if previous bult up string
                if buid_string_size > 0:
                    final_string = final_string + build_string
                    build_string = []
                    build_string_index = 0
                    buid_string_size = 0
                
                    # now since it ha broke here check again for starting of the part string
                    if character == part_string_map[build_string_index]:
                        build_string.append(character)
                        buid_string_size = buid_string_size + 1
                        build_string_index = build_string_index + 1
                    else:
                        final_string.append(character)
                else:
                    final_string.append(character)
            print(final_string , build_string)
        

        if buid_string_size > 0:
            final_string = final_string + build_string
        
        print("\nfinal_string")
        print(final_string)
        return ("".join(final_string))







        # while position < size:
        #     pointing_character = part_string_map[build_string_index]
        #     current_character = s[position]
        #     if current_character == pointing_character:
        #         buid_string_size = buid_string_size + 1
        #         build_string_index = build_string_index + 1
        #         for index in range(position + 1, min((position + part_string_size) , size)):
        #             temp_character = s[index]
        #             temp_part_character = part_string_map[build_string_index]
        #             if temp_character == temp_part_character:
        #                 buid_string_size = buid_string_size + 1
        #                 build_string_index = build_string_index + 1

      