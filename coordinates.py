from typing import NamedTuple

class Coordinate(NamedTuple):
    Latitude: float
    longitude: float

def get_coordinate() -> Coordinate:
    return Coordinate(Latitude=50.061796, longitude=14.438470)