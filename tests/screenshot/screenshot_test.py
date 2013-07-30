__author__ = 'i.pavlov'

import unittest
import os
import json
import math, operator

from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities

from tests.BrowserTestCase import BrowserTestCase

from core.dali_core import DaliCore

from PIL import Image
import numpy


class ScreenshotTestCase(BrowserTestCase):
    def setUp(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://localhost:4444/wd/hub"
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        # NOTE current_directory is used in webserver setup
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        super(ScreenshotTestCase, self).setUp()

    def tearDown(self):
        self.driver.close()
        try:
            os.remove(self.screenshot_name)
        except OSError:
            pass

        super(ScreenshotTestCase, self).tearDown()

    def test_core_screenshot_file_creation(self):
        self.screenshot_name = self.core.take(self.current_directory, {})
        self.assertTrue(os.path.exists(self.screenshot_name))

    def test_core_screenshot_image(self):
        self._loadPage("picture1")
        self.screenshot_name = self.core.take(self.current_directory, {})
        image1 = Image.open(self.screenshot_name)
        image2 = Image.open(self.current_directory + "/src/persistencia_de_la_memoria.png")

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)


if __name__ == "__main__":
    unittest.main()