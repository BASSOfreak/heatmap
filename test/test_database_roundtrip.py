import unittest

from db_connection.db_methods import get_gps_file_by_name, insert_gps_file
from db_connection.db_setup import clear_db, setup_db
from gpsconverter.ConvertGpsFile import parseFitFile
import module_variables

class Test_DataBase_Roundtrip(unittest.TestCase):
    def setUp(self):
        clear_db(module_variables.TESTDBNAME)
        setup_db(module_variables.TESTDBNAME)

    def tearDown(self):
        clear_db(module_variables.TESTDBNAME)
    
    def test1(self):
        
        # read file
        data_folder = 'test/test_data'
        file_name = 'Corsa_pomeridiana.fit'
        gpsfile_in = parseFitFile(data_folder, file_name)
        # show name
        print('file name: ' + gpsfile_in.name)
        # insert into db
        insert_gps_file(gpsfile_in, module_variables.TESTDBNAME)
        # get file from db
        gps_file_out = get_gps_file_by_name(file_name, 
                module_variables.TESTDBNAME)
        # compare values
        self.assertEqual(gpsfile_in.name, gps_file_out.name)
        self.assertEqual(gpsfile_in.date, gps_file_out.date)
        self.assertListEqual(
                gpsfile_in.get_points(), gps_file_out.get_points())
        self.assertEqual(gpsfile_in.hash, gps_file_out.hash)
        self.assertEqual(gpsfile_in.distance, gps_file_out.distance)
        