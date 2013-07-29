__author__ = 'i.pavlov'

import unittest
import os

from core.compare.pixel_diff import diff


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_pixel_diff(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        file1 = current_directory + "/pic1.png"
        file2 = current_directory + "/pic2.png"

        difference = diff(file1, file2, current_directory + "/out.png")
        self.assertEqual(0.25, difference)


if __name__ == "__main__":
    unittest.main()