import folium

from db_connection.db_methods import get_all_files_in_db, get_gps_file_by_name
from gpsfile.GpsFileWithPts import GpsFileWithPts
import module_variables


def createMap():
    m = folium.Map(location=[52.527455650269985, 13.333634929731488], zoom_start=11)
    add_points_to_map(m)
    m.save("tempMap.html")

def add_points_to_map(map: folium.Map):
    list_of_all_file_names = get_all_files_in_db(module_variables.DBNAME)
    for file_name in list_of_all_file_names:
        gps_file = get_gps_file_by_name(file_name, module_variables.DBNAME)
        trail_coordinates = gps_file.get_points()
        folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(map)

if __name__ == "__main__":
    createMap()
