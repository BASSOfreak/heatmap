import unittest
import numpy as np
from math import pi

from gpsconverter.main import get_direction
class Test_GpsConverter(unittest.TestCase):
    debug = False
    def test1(self):
        # north
        north = np.array([0,1])
        direction = get_direction(north)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - 0) < 0.01)

        # south
        south = np.array([0,-1])
        direction = get_direction(south)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - pi) < 0.01)

        # east
        east = np.array([1,0])
        direction = get_direction(east)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - pi/2) < 0.01)

        # west
        west = np.array([-1,0])
        direction = get_direction(west)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - (pi + pi/2)) < 0.01)

        # north east
        northeast = np.array([1,1])
        direction = get_direction(northeast)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - pi/4) < 0.01)

        # south west
        southwest = np.array([-1,-1])
        direction = get_direction(southwest)
        if self.debug: print(direction)
        self.assertTrue(abs(direction - (pi + pi/4)) < 0.01)
