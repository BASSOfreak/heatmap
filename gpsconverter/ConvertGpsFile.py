import xml.etree.ElementTree as ET
import numpy as np
from math import pi
import fitdecode
from pathlib import Path
from gpsconverter.StringListConverter import points

def convertFile(data_folder_in: str, file_name_in:str, output_folder_in: str):
    # load file
    data_folder = data_folder_in
    file_name = file_name_in

    output = []

    match Path(file_name).suffix:
        case ".fit":
            output = parseFitFile(data_folder, file_name)
        case ".gpx":
            output = parseGpsFile(data_folder, file_name)
        case _:
            print("file type not supported")
            return
    stack = np.stack(output)
    #print(stack)
    #print(stack[0,:] - stack[1,:])

    file = open(output_folder_in + file_name, 'w')
    out_string = ""
    for line in stack:
        line_string = str(line[0]) + ";" + str(line[1]) + '\n'
        out_string += line_string

    GpsFileWithPoints(
            file_name,
            convert_string_to_list(out_string), 
            date, 
            duration,
            distance, 
            hash_value)

def parseGpsFile(data_folder, file_name):

    data = open(data_folder + file_name).read()
    tree = ET.fromstring(data)

    num_of_pts = len(tree[1][2].findall('{http://www.topografix.com/GPX/1/1}trkpt'))
    output = []
    counter = 0
    # fetch all points from file
    for trkpt in tree.iter('{http://www.topografix.com/GPX/1/1}trkpt'):
        trkpt_vec = np.array([float(trkpt.get('lat')), float(trkpt.get('lon'))])
        #print(trkpt_vec)
        output.append(trkpt_vec)
        #counter = counter + 1
        if counter > 10:
            break

    return output

def parseFitFile(data_folder, file_name):
    counter = 0
    output = []
    with fitdecode.FitReader(data_folder + file_name) as fit:
        for frame in fit:
            #counter = counter + 1
            #print("frame of type" + str(frame.frame_type))
            if frame.frame_type == fitdecode.FIT_FRAME_DATA:
                #print("is fit frame data")
                #print('non_existent_field:', frame.get_value('non_existent_field', fallback='field not present'))
                if frame.has_field('position_lat') and frame.has_field('position_long'):
                    #print("asda")
                    #print('latitude:', frame.get_value('position_lat') / ((2**32)/360))
                    #print('longitude:', frame.get_value('position_long') / ((2**32)/360))
                    trkpt_vec = np.array([frame.get_value('position_lat') /
                            ((2**32)/360), frame.get_value('position_long') / 
                            ((2**32)/360)])
                    output.append(trkpt_vec)

            if counter > 120:
                break

    return output

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



if __name__ == "__main__":
    convertGpsFile()
