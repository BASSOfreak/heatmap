import unittest
import numpy as np
from math import pi
from gpsconverter.StringListConverter import *
from module_variables import *
class Test_StringListConverter(unittest.TestCase):
    def test1(self):
        # create list
        start_list = [[52.0001, 14.0110],[53.0001, 15.9999]]
        if DEBUG_MODE:
            print(start_list)
        # convert to string
        as_string = convert_list_to_string(start_list)
        # convert back to list
        back_to_list = convert_string_to_list(as_string)
        # ensure that they are equal
        
        self.assertListEqual(back_to_list, start_list)
