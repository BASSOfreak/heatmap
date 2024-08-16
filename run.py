from gpsconverter.ConvertGpsFile import convertFile
from plotting.MapPlot import createMap
from db_connection.db_methods import *
from gpsconverter.HashFile import hash_file
from db_feeder import insert_files_into_db 


import gzip
exampleString = 'abcdefghijklm'
compressed_value = gzip.compress(bytes(exampleString, 'utf-8'))
plain_string_again = gzip.decompress(compressed_value).decode('utf-8')
print(plain_string_again)
