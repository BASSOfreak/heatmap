from pathlib import Path

class GpsFile:
    def __init__(self, in_name: str, in_date, in_duration,
                 in_distance, in_hash):
        self.name = in_name
        self.duration = in_duration
        self.date = in_date
        self.distance = in_distance
        self.hash = in_hash
