import module_variables
from os import listdir
from os.path import isfile, join
from gpsconverter.ConvertGpsFile import convertFile
from db_connection.db_methods import insert_gps_file
from gpsfile.BlobHandling import convert_into_binary
from gpsconverter.HashFile import hash_file
from gpsfile.GpsFileWithPts import GpsFileWithPts
import module_variables

def insert_files_into_db():
    input_folder = module_variables.INPUT_FILES_LOCATION
    # loop through all input files
    onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    for file_name in onlyfiles:
        print(file_name)
        gpsfile_in = parseFitFile(file_name)
        # show name
        print('file name: ' + gpsfile_in.name)
        # insert into db
        insert_gps_file(gpsfile_in, module_variables.TESTDBNAME)
