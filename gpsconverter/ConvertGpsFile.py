import xml.etree.ElementTree as ET
import numpy as np
from math import pi

def run():
    # load file
    data_folder = "data/"
    data = open(data_folder + "file1.gpx").read()
    tree = ET.fromstring(data)

    num_of_pts = len(tree[1][2].findall('{http://www.topografix.com/GPX/1/1}trkpt'))
    output = []
    counter = 0
    # fetch all points from file
    for trkpt in tree.iter('{http://www.topografix.com/GPX/1/1}trkpt'):
        trkpt_vec = np.array([float(trkpt.get('lat')), float(trkpt.get('lon'))])
        print(trkpt_vec)
        output.append(trkpt_vec)
        counter = counter + 1
        if counter > 10:
            break

    stack = np.stack(output)
    print(stack)
    print(stack[0,:] - stack[1,:])

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
    run()
