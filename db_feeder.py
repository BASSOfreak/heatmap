import module_variables
from os import listdir
from os.path import isfile, join
from gpsconverter.ConvertGpsFile import convertFile
from db_connection.db_methods import insert_gps_file
from gpsfile.BlobHandling import convert_into_binary
from gpsconverter.HashFile import hash_file
from gpsfile.GpsFileWithPts import GpsFileWithPts

def insert_files_into_db():
    input_folder = module_variables.INPUT_FILES_LOCATION
    # loop through all input files
    onlyfiles = [f for f in listdir(input_folder) if isfile(join(input_folder, f))]
    for file_name in onlyfiles:
        print(file_name)
        convertFile(input_folder, file_name, module_variables.TEMP_OUTPUT_FILES_LOCATION)
        convertedFileLocation = str(module_variables.TEMP_OUTPUT_FILES_LOCATION + file_name)
        print(convertedFileLocation)
        gpsFile = GpsFileWithPts(
                file_name,
                convert_into_binary(convertedFileLocation),
                '01-01-2024',
                10,
                10,
                hash_file(convertedFileLocation)
            )
        insert_gps_file(gpsFile)

