import module_variables
from os import listdir
from os.path import isfile, join
from gpsconverter.ConvertGpsFile import convertFile
from db_connection.db_methods import (
    insert_gps_file,
    check_if_in_db
)
from gpsconverter.HashFile import hash_file
from gpsfile.GpsFileWithPts import GpsFileWithPts

def insert_files_into_db():
    input_folder = module_variables.INPUT_FILES_LOCATION
    # loop through all input files
    onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    for file_name in onlyfiles:
        print(file_name)
        if not check_if_in_db(module_variables.DBNAME, file_name):
            gpsfile_in = convertFile(input_folder, file_name)
            # show name
            print('file name of gps file to insert: ' + gpsfile_in.name)
            # insert into db
            insert_gps_file(gpsfile_in, module_variables.DBNAME)
