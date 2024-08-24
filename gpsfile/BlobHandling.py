import gzip
from gpsconverter.StringListConverter import convert_list_to_string
from gpsconverter.StringListConverter import convert_string_to_list

def convert_into_binary(file_path: str):
    with open(file_path, 'rb') as file:
        binary = file.read()
    return binary

def write_blob_to_file(blob, file_path):
    with open(file_path, 'wb') as file:
        file.write(blob)

def create_blob_from_points(in_points):
    points_as_string = convert_list_to_string(in_points)
    return gzip.compress(bytes(points_as_string, 'utf-8'))

def create_points_from_blob(in_blob):
    points_as_string = gzip.decompress(in_blob).decode('utf-8')
    return convert_string_to_list(points_as_string) 
