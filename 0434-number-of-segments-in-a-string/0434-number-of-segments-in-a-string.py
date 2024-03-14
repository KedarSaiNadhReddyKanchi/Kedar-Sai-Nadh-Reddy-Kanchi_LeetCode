class Solution:
    def countSegments(self, s: str) -> int:
        
        if len(s) == 0:
            return 0
        
        previous_character = None
        segment_count = 0
        for character in s:
            if character == " ":
                if previous_character is None:
                    previous_character = " "
                elif previous_character == " ":
                    continue
                else:
                    segment_count = segment_count + 1
                    previous_character = " "
            else:
                previous_character = character
            print(f"segment_count = {segment_count} and for character = {character}")
        
        print(f"previous_character = {previous_character}")
        if previous_character != " ":
            return (segment_count + 1)
        return segment_count
                    
                    
        