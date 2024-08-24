from gpsfile.GpsFileWithPts import GpsFileWithPts
from gpsfile.BlobHandling import convert_into_binary
from gpsfile.BlobHandling import create_points_from_blob
from gpsfile.BlobHandling import create_blob_from_points
import module_variables
import sqlite3
from gpsconverter.HashFile import hash_file

def print_all_files():
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    res = cur.execute('SELECT name FROM GPSFILES;')
    record = res.fetchall()
    for row in record:
        print(row[0])

def get_gps_file_by_name(name: str):
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    res = cur.execute(f"""SELECT name, file, date, duration, distance,
                      hash_of_file FROM GPSFILES WHERE name = \'{name}\';""")
    record = res.fetchone()
    gpsFile = GpsFileWithPts(record[0], record[1])

def insert_gps_file_from_path(file_path: str):
    # read GPS file
    binary_blob = convert_into_binary(file_path)
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    fname = 'fname'
    hash_of_file = hash_file(file_path)
    res = cur.execute("""INSERT INTO GPSFILES (name, date, distance,
        duration, file, hash_of_file) VALUES (NULL, ?,?,?,?,?, ?);""",\
        (fname, '01.01.2024', 10, 10, binary_blob, hash_of_file))
    con.commit()

def insert_gps_file(in_file: GpsFileWithPts):
    # read GPS file
    binary_blob = create_blob_from_points(file_path)
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    fname = 'fname'
    res = cur.execute("""INSERT INTO GPSFILES (name, date, distance, duration,
        file) VALUES (?,?,?,?,?);""",\
        (fname, '01.01.2024', 10, 10, binary_blob))
    con.commit()

# order is: name, file, date, duration, distance, hash_of_file
def create_gps_file_from_full_params(record_row):
    points = create_points_from_blob(record_row[1])
    gpsFile = GpsFileWithPts(
            record_row[0], # name 
            points, # points
            record_row[2], # date
            record_row[3], # duration
            record_row[4], # distance
            record_row[5]) # hash
    return gpsFile

def delete_all_files():
    conf = input('type \'yes\' to confirm deleting all files in database')
    if conf == 'yes':
        con = sqlite3.connect(module_variables.DBNAME)
        cur = con.cursor()
        res = cur.execute("""DELETE FROM GPSFILES;""")
        con.commit()
    else:
        print('not doing anything. bye.')

