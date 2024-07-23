from pathlib import Path

class GpsFile:
    def __init__(self, in_path: str):
        self.path = Path(in_path)
        self.name: str = self.path.name
        self.number_pts: int = 0

        self.pts = []

        self.load_pts_from_path()

    def set_points(self, in_pts):
        self.pts = in_points
        self.number_pts = len(in_pts)

    def get_points(self):
        return self.pts

    def load_pts_from_path(self):
        with self.path.open() as file:
            for line in file:
                print(line)
                vals = line.split(';')
                self.pts.append((float(vals[0]), float(vals[1])))
