class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # map to store the distinct labels of the balls
        balls_map = {}

        # initialize a color map to store the which ball is assigned which color
        # in this case we would have only distinct colors as the keys 
        # and for each color a inner map with the key as the ball number
        colors_map = {}

        # maintain a size variable for the number of distinct colors present
        number_of_distinct_colors = 0

        result = []

        # now loop over the queries now 
        for ball_number , ball_color in queries:

            # get the current color of the ball
            current_ball_color = None if (ball_number not in balls_map) else balls_map[ball_number]

            # check if the ball is colored at this point or not 
            if current_ball_color is None:
                # then that means the ball is not colored at this point of time. 
                # so add this color as the value to the ball 
                balls_map[ball_number] = ball_color

                # now we need to check if the ball_color is present in the colors map or not
                if ball_color not in colors_map:
                    # then this means that this color has not been previously used
                    colors_map[ball_color] = 1
                    number_of_distinct_colors = number_of_distinct_colors + 1
                else:
                    # then this means that the ball color is already existing
                    # in the colors map since it would have been used color another ball
                    # so that this point of time we just simply 
                        # add the ball number as another key within the ball color
                    colors_map[ball_color] = colors_map[ball_color] + 1
            else:
                # at this point it means the current ball is previsouly colored
                # so we need to first remove the ball from that color before reassigning
                colors_map[current_ball_color] = colors_map[current_ball_color] - 1

                # now since we have removed the ball from the previous color
                # we need to check if there are any balls previsouly colored with that color
                # and if not then remove the color from the colors map so that it would not be considered as a distinct color
                if colors_map[current_ball_color] == 0:
                    del colors_map[current_ball_color]
                    number_of_distinct_colors = number_of_distinct_colors - 1

                # now add the new color to the colors map 
                if ball_color not in colors_map:
                    colors_map[ball_color] = 1
                    number_of_distinct_colors = number_of_distinct_colors + 1
                else:
                    colors_map[ball_color] = colors_map[ball_color] + 1
                
                # at the end add the new color to the current ball
                balls_map[ball_number] = ball_color

            # finally at the end add the number of distinct colors at this point
            result.append(number_of_distinct_colors)

        return result


