__author__ = 'i.pavlov'

import unittest
import os

from dali import Dali

from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities

from tests.config import Config
from tests.BrowserTestCase import BrowserTestCase

from PIL import Image
import numpy


class TakeScreenshotScenarioTestCase(BrowserTestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))

        super(TakeScreenshotScenarioTestCase, self).setUp()

    def tearDown(self):
        self.driver.quit()
        try:
            os.remove(self.screenshot1)
        except (OSError, AttributeError):
            pass

        try:
            os.remove(self.screenshot2)
        except (OSError, AttributeError):
            pass

        super(TakeScreenshotScenarioTestCase, self).tearDown()

    def test_scenario_firefox(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        dali = Dali(self.driver)

        # driver can navigate through himself
        self.driver.get(self.page_url('colored'))
        self.screenshot1 = dali.take_screenshot(
            resolution="800x600",
            path_to_save=self.current_directory,
        )

        # and we can use scenario with preset resolution
        def scenario(driver):
            driver.get(self.page_url('colored'))
        self.screenshot2 = dali.take_screenshot(
            resolution="800x600",
            scenario=scenario,
            scenario_args=self.driver,
            path_to_save=self.current_directory,
        )

        self.assertTrue(os.path.exists(self.screenshot1))
        self.assertTrue(os.path.exists(self.screenshot2))

        image1 = Image.open(self.screenshot1)
        image2 = Image.open(self.screenshot2)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_scenario_chrome(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        dali = Dali(self.driver)

        # driver can navigate through himself
        self.driver.get(self.page_url('colored'))
        self.screenshot1 = dali.take_screenshot(
            resolution="800x600",
            path_to_save=self.current_directory,
        )

        # and we can use scenario with preset resolution
        def scenario(driver):
            driver.get(self.page_url('colored'))
        self.screenshot2 = dali.take_screenshot(
            resolution="800x600",
            scenario=scenario,
            scenario_args=self.driver,
            path_to_save=self.current_directory,
        )

        self.assertTrue(os.path.exists(self.screenshot1))
        self.assertTrue(os.path.exists(self.screenshot2))

        image1 = Image.open(self.screenshot1)
        image2 = Image.open(self.screenshot2)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    @unittest.expectedFailure
    def test_scenario_opera(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        dali = Dali(self.driver)

        # driver can navigate through himself
        self.driver.get(self.page_url('colored'))
        self.screenshot1 = dali.take_screenshot(
            resolution="800x600",
            path_to_save=self.current_directory,
        )

        # and we can use scenario with preset resolution
        def scenario(driver):
            driver.get(self.page_url('colored'))
        self.screenshot2 = dali.take_screenshot(
            resolution="800x600",
            scenario=scenario,
            scenario_args=self.driver,
            path_to_save=self.current_directory,
        )

        self.assertTrue(os.path.exists(self.screenshot1))
        self.assertTrue(os.path.exists(self.screenshot2))

        image1 = Image.open(self.screenshot1)
        image2 = Image.open(self.screenshot2)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_scenario_internetexplorer(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        dali = Dali(self.driver)

        # driver can navigate through himself
        self.driver.get(self.page_url('colored'))
        self.screenshot1 = dali.take_screenshot(
            resolution="800x600",
            path_to_save=self.current_directory,
        )

        # and we can use scenario with preset resolution
        def scenario(driver):
            driver.get(self.page_url('colored'))
        self.screenshot2 = dali.take_screenshot(
            resolution="800x600",
            scenario=scenario,
            scenario_args=self.driver,
            path_to_save=self.current_directory,
        )

        self.assertTrue(os.path.exists(self.screenshot1))
        self.assertTrue(os.path.exists(self.screenshot2))

        image1 = Image.open(self.screenshot1)
        image2 = Image.open(self.screenshot2)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

if __name__ == "__main__":
    unittest.main()