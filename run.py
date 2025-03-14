from gpsconverter.ConvertGpsFile import (
    parseFitFile, 
    parseGpsFile
)
from db_connection.db_methods import (
    insert_gps_file, 
    get_gps_file_by_name, 
    print_all_files,
    check_if_in_db,
    get_all_files_in_db_filtered
)
from db_connection.db_setup import clear_db, setup_db
from db_feeder import insert_files_into_db
from plotting.MapPlot import createMap
import module_variables
from plotting.heatmap_overlay import create_image_from_all_files

#clear_db(module_variables.DBNAME)
#setup_db(module_variables.DBNAME)
#insert_files_into_db()
#createMap()
#create_image_from_all_files(module_variables.DBNAME)
#print_all_files(module_variables.DBNAME)
#print(check_if_in_db(module_variables.DBNAME, "2024-08-24-13-23-08.fit"))
print(get_all_files_in_db_filtered(module_variables.DBNAME,start_date="2024-06-16"))