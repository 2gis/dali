import unittest
import os
import json
import time
from tests.config import Config

from selenium.webdriver import Remote
from selenium.webdriver import DesiredCapabilities

from tests.BrowserTestCase import BrowserTestCase

from common.core.dali_core import DaliCore

from PIL import Image
import numpy


class ScreenshotTestCase(BrowserTestCase):
    def setUp(self):
        # NOTE current_directory is used in webserver setup
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        super(ScreenshotTestCase, self).setUp()

    def tearDown(self):
        self.driver.quit()
        try:
            os.remove(self.first_screenshot)
        except (OSError, AttributeError):
            pass
        try:
            os.remove(self.second_screenshot)
        except (OSError, AttributeError):
            pass

        super(ScreenshotTestCase, self).tearDown()


    def test_core_screenshot_image_firefox(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("picture1")
        self.first_screenshot = self.core.take(self.current_directory, {})
        self.second_screenshot = self.core.take(self.current_directory, {})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_image_chrome(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("picture1")
        self.first_screenshot = self.core.take(self.current_directory, {})
        self.second_screenshot = self.core.take(self.current_directory, {})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_image_opera(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("picture1")
        self.first_screenshot = self.core.take(self.current_directory, {})
        self.second_screenshot = self.core.take(self.current_directory, {})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_image_internetexplorer(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("picture1")
        self.first_screenshot = self.core.take(self.current_directory, {})
        self.second_screenshot = self.core.take(self.current_directory, {})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_disable_animation_firefox(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("animation")
        self.first_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.load_page("animation")
        #sleep to get another state of animation
        time.sleep(0.5)
        self.second_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_disable_animation_chrome(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("animation")
        self.first_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.load_page("animation")
        #sleep to get another state of animation
        time.sleep(0.5)
        self.second_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_disable_animation_opera(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("animation")
        self.first_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.load_page("animation")
        #sleep to get another state of animation
        time.sleep(0.5)
        self.second_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_disable_animation_internetexplorer(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("animation")
        self.first_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.load_page("animation")
        #sleep to get another state of animation
        time.sleep(0.5)
        self.second_screenshot = self.core.take(self.current_directory, {"disable_animation": "True"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_hide_elements_firefox(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.FIREFOX,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("hide_elements1")
        self.first_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.load_page("hide_elements2")
        self.second_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_hide_elements_chrome(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("hide_elements1")
        self.first_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.load_page("hide_elements2")
        self.second_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_hide_elements_opera(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.OPERA,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("hide_elements1")
        self.first_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.load_page("hide_elements2")
        self.second_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)

    def test_core_screenshot_hide_elements_internetexplorer(self):
        # Dali setup
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.INTERNETEXPLORER,
            command_executor="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port)
        )
        self.core = DaliCore()
        self.core.init(self.driver.command_executor._url, json.dumps(self.driver.capabilities))

        self.load_page("hide_elements1")
        self.first_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.load_page("hide_elements2")
        self.second_screenshot = self.core.take(self.current_directory, {"hide_elements": "#pic"})

        self.assertTrue(os.path.exists(self.first_screenshot))
        self.assertTrue(os.path.exists(self.second_screenshot))

        image1 = Image.open(self.first_screenshot)
        image2 = Image.open(self.second_screenshot)

        matrix1 = numpy.asarray(image1)
        matrix2 = numpy.asarray(image2)

        numpy.testing.assert_array_equal(matrix1, matrix2)


if __name__ == "__main__":
    unittest.main()