from gpsfile.GpsFile import GpsFile
from pathlib import Path

class GpsFileWithPts(GpsFile):
    def __init__(self, in_path: str):
        self.path = Path(in_path)
        self.name: str = self.path.name
        self.number_pts: int = 0

        self.pts = []

        self.__load_pts_from_path()

    def __init__(self, in_name: str, in_points, in_date, in_duration,
                 in_distance, in_hash):
        super(GpsFileWithPts, self).__init__(in_name, in_date, in_duration,
                                         in_distance, in_hash)
        self.pts = in_points

    def set_points(self, in_pts):
        self.pts = in_pts
        self.number_pts = len(in_pts)

    def get_points(self):
        return self.pts

