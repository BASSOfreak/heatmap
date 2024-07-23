from gpsfile.GpsFile import GpsFile
import module_variables
import sqlite3

def get_gps_file_by_name(name: str):
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    res = cur.execute(f'SELECT file FROM GPSFILES WHERE name = \'{name}\';')
    print(res.fetchall())
    #GpsFile()

def insert_gps_file(file_path: str):
    con = sqlite3.connect(module_variables.DBNAME)
    cur = con.cursor()
    fname = 'fname'
    res = cur.execute(f'INSERT INTO GPSFILES (name) VALUES ({fname});')
    con.commit()


def str_to_db_command(input: str):
    return '\'' + input + '\''

