from gpsconverter.ConvertGpsFile import parseFitFile
from db_connection.db_methods import (
    insert_gps_file, 
    get_gps_file_by_name, 
    print_all_files
)
from db_connection.db_setup import clear_db, setup_db
from db_feeder import insert_files_into_db
import module_variables

#clear_db(module_variables.DBNAME)
#setup_db(module_variables.DBNAME)
#print_all_files(module_variables.DBNAME)
insert_files_into_db()
