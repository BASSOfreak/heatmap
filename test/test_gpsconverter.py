import unittest
import numpy as np
from math import pi
from module_variables import *

from gpsconverter.DirectionHandling import get_direction
class Test_DirectionHandling(unittest.TestCase):
    def testDirections(self):
        # north
        north = np.array([0,1])
        direction = get_direction(north)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - 0) < 0.01)

        # south
        south = np.array([0,-1])
        direction = get_direction(south)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - pi) < 0.01)

        # east
        east = np.array([1,0])
        direction = get_direction(east)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - pi/2) < 0.01)

        # west
        west = np.array([-1,0])
        direction = get_direction(west)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - (pi + pi/2)) < 0.01)

        # north east
        northeast = np.array([1,1])
        direction = get_direction(northeast)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - pi/4) < 0.01)

        # south west
        southwest = np.array([-1,-1])
        direction = get_direction(southwest)
        if DEBUG_MODE: print(direction)
        self.assertTrue(abs(direction - (pi + pi/4)) < 0.01)

    @unittest.skip("not yet implemented")
    def testStraightLine(self):
        a = [[1,0],[2,0],[3,0],[4,0],[5,0]]
        res = []
        self.assertListEqual(res, [[1,0],[5,0]])

    @unittest.skip("not yet implemented")
    def testRightTurn(self):
        a = [[1,0],[2,0],[3,0],[3,1],[3,2]]
        res = []
        self.assertListEqual(res, [[1,0],[3,0],[3,2]])