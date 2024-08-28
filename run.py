from gpsconverter.ConvertGpsFile import parseFitFile
from db_connection.db_methods import insert_gps_file, get_gps_file_by_name


# read file
data_folder = 'data/'
file_name = 'Evening_Ride.fit'
gpsfile_in = parseFitFile(data_folder, file_name)
# show name
print('file name: ' + gpsfile_in.name)
# insert into db
insert_gps_file(gpsfile_in)
# get file from db
gps_file_out = get_gps_file_by_name(file_name)
# show name
print(gps_file_out.name)


