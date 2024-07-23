import folium
from gpsfile.GpsFile import GpsFile

def createMap():
    m = folium.Map(location=[52.527455650269985, 13.333634929731488], zoom_start=11)

    gps_file = GpsFile('./file.txt')

    trail_coordinates = gps_file.get_points()

    folium.PolyLine(trail_coordinates, tooltip="Coast").add_to(m)

    m.save("tempMap.html")

if __name__ == "__main__":
    createMap()
