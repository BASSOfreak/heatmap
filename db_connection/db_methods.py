from gpsfile.GpsFileWithPts import GpsFileWithPts
from gpsfile.BlobHandling import convert_into_binary
from gpsfile.BlobHandling import create_points_from_blob
from gpsfile.BlobHandling import create_blob_from_points
import sqlite3
from gpsconverter.HashFile import hash_file
from datetime import datetime

def get_all_files_in_db(path_to_db: str) -> list:
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    res = cur.execute('SELECT name FROM GPSFILES;')
    record = res.fetchall()
    output = []
    for row in record:
        output.append(row[0])

    return output

def print_all_files(path_to_db: str):
    all_files = get_all_files_in_db(path_to_db)
    for name in all_files:
        print(name)
    
def check_if_in_db(path_to_db: str, file_name: str) -> bool:
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    res = cur.execute(f"""SELECT EXISTS (SELECT 1 FROM GPSFILES WHERE name = \'{file_name}\');""")
    val = res.fetchone()
    if val[0] == 1:
        return True
    else:
        return False

def get_gps_file_by_name(name: str, path_to_db: str) -> GpsFileWithPts:
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    res = cur.execute(f"""SELECT name, file, date, duration, distance,
                      hash_of_file FROM GPSFILES WHERE name = \'{name}\';""")
    record = res.fetchone()
    gpsFile = create_gps_file_from_full_params(record)
    return gpsFile

def insert_gps_file_from_path(file_path: str, path_to_db: str):
    # read GPS file
    binary_blob = convert_into_binary(file_path)
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    fname = 'fname'
    hash_of_file = hash_file(file_path)
    res = cur.execute("""INSERT INTO GPSFILES (id, name, date, distance,
        duration, file, hash_of_file) VALUES (NULL, ?,?,?,?,?, ?);""",\
        (fname, '01.01.2024', 10, 10, binary_blob, hash_of_file))
    con.commit()

def insert_gps_file(in_file: GpsFileWithPts, path_to_db: str):
    # read GPS file
    name = in_file.name
    date = in_file.date
    distance = in_file.distance
    duration = in_file.duration
    binary_blob = create_blob_from_points(in_file.get_points())
    hash = in_file.hash
    con = sqlite3.connect(path_to_db)
    cur = con.cursor()
    cur.execute("""INSERT INTO GPSFILES (id, name, date, distance,
            duration, file, hash_of_file) VALUES (NULL,?,?,?,?,?,?);""",\
            (name, date, distance, duration, binary_blob, hash))
    con.commit()

# order is: name, file, date, duration, distance, hash_of_file
def create_gps_file_from_full_params(record_row):
    points = create_points_from_blob(record_row[1])
    # print("datetime value from db: " + record_row[2])
    # timestamp value from db
    timestamp_output = record_row[2]
    timestamp = datetime.strptime(timestamp_output.split('+')[0], 
            '%Y-%m-%d %H:%M:%S')
    gpsFile = GpsFileWithPts(
            record_row[0], # name 
            points, # points
            timestamp, # date
            record_row[3], # duration
            record_row[4], # distance
            record_row[5]) # hash
    return gpsFile

def delete_all_files(path_to_db: str):
    conf = input('type \'yes\' to confirm deleting all files in database')
    if conf == 'yes':
        con = sqlite3.connect(path_to_db)
        cur = con.cursor()
        res = cur.execute("""DELETE FROM GPSFILES;""")
        con.commit()
    else:
        print('not doing anything. bye.')

