__author__ = 'i.pavlov'

import unittest
import os
import json
from tests.config import Config

from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities

from core.dali_core import DaliCore


class ResizeTestCase(unittest.TestCase):
    def setUp(self):
        # NOTE current_directory is used in webserver setup
        self.current_directory = os.path.dirname(os.path.abspath(__file__))

    def tearDown(self):
        self.driver.quit()


    def test_core_screenshot_resize_firefox(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        resolutions = ["800x600", "1024x768", "1280x1024", "1366x768"]
        for resolution in resolutions:
            self.core.resize(resolution)
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            actual_resolution = "{width}x{height}".format(width=width, height=height)
            self.assertEqual(resolution, actual_resolution)

    def test_core_screenshot_resize_chrome(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        resolutions = ["800x600", "1024x768", "1280x1024", "1366x768"]
        for resolution in resolutions:
            self.core.resize(resolution)
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            actual_resolution = "{width}x{height}".format(width=width, height=height)
            self.assertEqual(resolution, actual_resolution)

    @unittest.expectedFailure
    def test_core_screenshot_resize_opera(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        resolutions = ["800x600", "1024x768", "1280x1024", "1366x768"]
        for resolution in resolutions:
            self.core.resize(resolution)
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            actual_resolution = "{width}x{height}".format(width=width, height=height)
            self.assertEqual(resolution, actual_resolution)

    def test_core_screenshot_resize_internetexplorer(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        resolutions = ["800x600", "1024x768", "1280x1024", "1366x768"]
        for resolution in resolutions:
            self.core.resize(resolution)
            size = self.driver.get_window_size()
            width = size["width"]
            height = size["height"]
            actual_resolution = "{width}x{height}".format(width=width, height=height)
            self.assertEqual(resolution, actual_resolution)

if __name__ == "__main__":
    unittest.main()