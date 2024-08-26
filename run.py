from gpsconverter.ConvertGpsFile import convertFile
from plotting.MapPlot import createMap
from db_connection.db_methods import *
from gpsconverter.HashFile import hash_file
from db_feeder import insert_files_into_db 

# read file
# show name
# insert into db
# get file from db
# show name
data_folder = 'data/'
file_name = '2024-06-08-16-54-18.fit'

import fitdecode

with fitdecode.FitReader(data_folder + file_name) as fit:
    for frame in fit:
        if frame.frame_type == fitdecode.FIT_FRAME_DATA:
            if frame.name == 'session':
                try:
                    print(frame.get_value('total_distance'))
                except:
                    print("no total distance")
                print(frame.name)
                print(frame.frame_type)
