class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        
        # first map out the indexes of the candles across the table by running a linear loop
            # store the positions of the candles in a hashmap
            # also store the nearest candle on the left hand side to the current position
                # this helps us to get the left end in a quick manner
                
        candle_positions = {}
        plate_positions = {}
        last_candle_position = -1
        first_instance_of_the_candle = -1
        total_plate_count = 0
        
        for position, symbol in enumerate(s):
            if symbol == "|":
                
                if last_candle_position != -1:
                    candle_positions[last_candle_position]["next"] = position
                
                candle_positions[position] = {}
                candle_positions[position]["previous"] = last_candle_position
                candle_positions[position]["next"] = -1
                last_candle_position = position
                if first_instance_of_the_candle == -1:
                    first_instance_of_the_candle = position
                else:
                    # add plateCountValue to the map
                    candle_positions[position]["plateCount"] = total_plate_count
            else:
                plate_positions[position] = "plate"
                candle_positions[position] = last_candle_position
                if last_candle_position != -1:
                    total_plate_count = total_plate_count + 1
                    
        if first_instance_of_the_candle == -1:
            zeros_list = [0] * len(queries)
            return zeros_list
                
        candle_positions[first_instance_of_the_candle]["plateCount"] = 0
        # print(f"first_instance_of_the_candle = {first_instance_of_the_candle}")
        # print("candle_positions")
        # print(candle_positions)
        # print("plate_positions")
        # print(plate_positions)
            
        # then now loop through the queries list
            # since at each position, we have the position of the last appeared candle
            # that would be the left hand side boundary
            # and similarly, we can find the right hand side boundary
                # by taking the value stored at the given right position
                
        result = []
        
        for query in queries:
            givenLeft = query[0]
            givenRight = query[1]

            if givenLeft in plate_positions:
                left_hand_side_boundary = candle_positions[givenLeft]
            else:
                left_hand_side_boundary = givenLeft
            
            if givenRight in plate_positions:
                right_hand_side_boundary = candle_positions[givenRight]
            else:
                right_hand_side_boundary = givenRight
            
            if left_hand_side_boundary == -1:
                left_hand_side_boundary = first_instance_of_the_candle
            
            if left_hand_side_boundary < givenLeft:
                left_hand_side_boundary = candle_positions[left_hand_side_boundary]['next']
            
            # print(f"left_hand_side_boundary = {left_hand_side_boundary} and right_hand_side_boundary = {right_hand_side_boundary}")
            

            # start = left_hand_side_boundary + 1
            # end = right_hand_side_boundary - 1
            # total_number_of_plates_in_between_candles = 0
            # while start <= end:
            #     if start in plate_positions:
            #         total_number_of_plates_in_between_candles = total_number_of_plates_in_between_candles + 1
            #     start = start + 1
            # result.append(total_number_of_plates_in_between_candles)
            if ((left_hand_side_boundary == -1) or (right_hand_side_boundary == -1)):
                result.append(0)
            else:
                if left_hand_side_boundary <= right_hand_side_boundary:
                    firstValue = candle_positions[left_hand_side_boundary]["plateCount"]
                    secondValue = candle_positions[right_hand_side_boundary]["plateCount"]
                    difference = secondValue - firstValue
                    result.append(difference)
                else:
                    result.append(0)
            
        # print("result")
        # print(result)
        return result