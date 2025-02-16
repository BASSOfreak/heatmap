import math
from db_connection.db_methods import get_all_files_in_db, get_gps_file_by_name
import module_variables
from PIL import Image as im
import numpy as np

def create_image_from_all_files(db_path: str):
    # create container for points from gps tracks
    initial_storage = np.zeros((module_variables.BIN_NUMBER_X, module_variables.BIN_NUMBER_Y), int)
    image_values = np.zeros((module_variables.BIN_NUMBER_X, module_variables.BIN_NUMBER_Y), np.uint8)
    # counter for highest overall value --> used for normalizing brightness
    highest_value_in_bins = 0
    
    file_names = get_all_files_in_db(db_path)
    for name in file_names:
        gps_file = get_gps_file_by_name(name, db_path)

        points = gps_file.get_points()
        points_for_current_track = np.zeros((module_variables.BIN_NUMBER_X, module_variables.BIN_NUMBER_Y), int)
        # loop through points
        for point in points:
            # transform point to local system
            x_value = -1 * (point[0] + module_variables.TRANSLATION_VALUE_X) * module_variables.SCALE_VALUE_X
            y_value = (point[1] + module_variables.TRANSLATION_VALUE_Y) * module_variables.SCALE_VALUE_Y
            bin_x = math.floor(x_value * module_variables.BIN_NUMBER_X)
            bin_y = math.floor(y_value * module_variables.BIN_NUMBER_Y)
            #print("points: " + str(x_value) + " " + str(y_value))
            #print("points: " + str(bin_x) + " " + str(bin_y))
            try:
                points_for_current_track[bin_x][bin_y] = 1
            except:
                #print("could not add point " + str(x_value) + "|" + str(y_value) + " to initial_storage")
                pass
        
        # add values for current track to overall storage
        initial_storage = initial_storage + points_for_current_track

    highest_value_in_bins = np.max(initial_storage)
    print("highest bin value: " + str(highest_value_in_bins))
    
    for dim1 in range(0,len(initial_storage)):
        for dim2 in range(0,len(initial_storage[0])):
            image_values[dim1][dim2] = get_normalized_color_value(initial_storage[dim1][dim2], 255, highest_value_in_bins)

    data = im.fromarray(image_values) 
    # saving the final output  
    # as a PNG file 
    data.save('gfg_dummy_pic.png', mode="RGBA")


def get_normalized_color_value(value: int, max_value: int, highest_value: int) -> np.uint8:
    return math.floor((value / highest_value) * max_value)


