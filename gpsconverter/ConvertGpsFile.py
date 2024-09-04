import xml.etree.ElementTree as ET
import numpy as np
from math import pi
import fitdecode
from pathlib import Path
from gpsconverter.HashFile import hash_file
from gpsconverter.StringListConverter import convert_string_to_list
from gpsfile.GpsFileWithPts import GpsFileWithPts

def convertFile(data_folder_in: str, file_name_in:str):
    # load file
    data_folder = data_folder_in
    file_name = file_name_in

    

    match Path(file_name).suffix:
        case ".fit":
            return parseFitFile(data_folder, file_name)
        case ".gpx":
            return parseGpsFile(data_folder, file_name)
        case _:
            print("file type not supported")
            return
        


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

    pts_list = pts_list_to_string(output)

    hash_value = hash_file(data_folder + file_name)

    gpsFile = GpsFileWithPts(
            file_name,
            convert_string_to_list(pts_list), 
            None, 
            None,
            None, 
            hash_value)
    
    return gpsFile

def parseFitFile(data_folder, file_name):
    if data_folder[-1] != '/':
        data_folder = data_folder + '/'

    counter = 0
    output = []
    total_dist = 0
    total_time = 0
    timestamp = ''
    with fitdecode.FitReader(data_folder + file_name) as fit:
        for frame in fit:
            #counter = counter + 1
            #print("frame of type" + str(frame.frame_type))
            if frame.frame_type == fitdecode.FIT_FRAME_DATA:
                #print("is fit frame data")
                #print('non_existent_field:', frame.get_value('non_existent_field', fallback='field not present'))
                if frame.has_field('position_lat') and frame.has_field('position_long'):
                    #print('latitude:', frame.get_value('position_lat') / ((2**32)/360))
                    #print('longitude:', frame.get_value('position_long') / ((2**32)/360))
                    trkpt_vec = np.array([frame.get_value('position_lat') /
                            ((2**32)/360), frame.get_value('position_long') / 
                            ((2**32)/360)])
                    output.append(trkpt_vec)
                
                if frame.name == 'session':
                    try:
                        total_dist = frame.get_value('total_distance')
                    except:
                        pass
                    try:
                        total_time = frame.get_value('total_elapsed_time')
                    except:
                        pass 
                    try:
                        timestamp = frame.get_value('start_time')
                        timestamp = timestamp.replace(tzinfo=None)
                    except:
                        pass
            #if counter > 120:
            #    break

    out_string = pts_list_to_string(output)

    hash_value = hash_file(data_folder + file_name)

    # convert time string to datetime
    print('timestamp: ' + str(timestamp))
    print('total_time: ' + str(total_time))
    #timestamp_datetime = datetime.strptime(timestamp.split('+')[0], 
    #                              '%Y-%m-%dT%H:%M:%S')

    gpsFile = GpsFileWithPts(
            file_name,
            convert_string_to_list(out_string), 
            timestamp, 
            total_time,
            total_dist, 
            hash_value)
    
    return gpsFile

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

def pts_list_to_string(in_list):
    stack = np.stack(in_list)

    out_string = ""
    for line in stack:
        line_string = str(line[0]) + ";" + str(line[1]) + '\n'
        out_string += line_string
    
    return out_string

if __name__ == "__main__":
    convertFile()
