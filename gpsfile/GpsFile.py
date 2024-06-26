class GpsFile:
    def __init__(self, in_path: str):
        self.path = in_path
        self.name: str =
        self.number_pts: int = 0

        self.points = []

    def set_points(self, in_points):
        self.points = in_points
        self.number_pts = len(in_points)

    def get_points(self):
        return self.points
