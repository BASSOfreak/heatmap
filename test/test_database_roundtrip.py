import unittest

from db_connection.db_methods import get_gps_file_by_name, insert_gps_file
from db_connection.db_setup import clear_db, setup_db
from gpsconverter.ConvertGpsFile import parseFitFile

class Test_DataBase_Roundtrip(unittest.TestCase):
    db_name = "test/test_data/test_db"
    def setUp(self):
        clear_db(self.db_name)
        setup_db(self.db_name)

    def tearDown(self):
        clear_db(self.db_name)
    
    def test1(self):
        
        # read file
        data_folder = 'test/test_data'
        file_name = 'Corsa_pomeridiana.fit'
        gpsfile_in = parseFitFile(data_folder, file_name)
        # show name
        print('file name: ' + gpsfile_in.name)
        # insert into db
        insert_gps_file(gpsfile_in)
        # get file from db
        gps_file_out = get_gps_file_by_name(file_name)
        # compare values
        self.assertEqual(gpsfile_in.name, gps_file_out.name)
        self.assertEqual(gpsfile_in.date, gps_file_out.date)
        