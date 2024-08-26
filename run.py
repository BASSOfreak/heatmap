from gpsconverter.ConvertGpsFile import parseFitFile


# read file
data_folder = 'data/'
file_name = 'Evening_Ride.fit'
gpsfile = parseFitFile(data_folder, file_name)
# show name
print('file name: ' + gpsfile.name)
# insert into db
# get file from db
# show name


