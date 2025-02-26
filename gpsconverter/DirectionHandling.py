from math import pi
import numpy as np

class DirectionContainer:
    def __init__():
        pass

    def add_point():
        pass

    

def get_direction(direction_vec):
    if direction_vec[0] == 0:
        if direction_vec[1] > 0:
            # north
            return 0
        else:
            return pi
    # negative value so it turns clockwise
    angle_val = -1 * np.arctan(direction_vec[1]/direction_vec[0])
    # add pi if in left quadrant
    if direction_vec[0] < 0:
        angle_val = angle_val + pi

    # add pi/2 so lowest value = 0
    angle_val = angle_val + pi / 2

    return angle_val