import unittest

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

from dali import Dali


class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://localhost:4444/wd/hub"
        )

    def tearDown(self):
        self.driver.quit()

    def test_example(self):
        def callback(driver):
            """
            :type driver: Remote
            """
            driver.implicitly_wait(2)
            driver.get("http://go.2gis.com/uvaw")
            driver.find_element_by_css_selector(".dg-traf-scores-wr").click()

        dali = Dali(self.driver)
        file1 = dali.take_screenshot(
            resolution="1024x768",
            scenario=callback,
            scenario_args=self.driver,
            path_to_save="/tmp",
            options={
                "disable_animation": "True",
                "hide_elements": ".dg-start-banner"
            }
        )

        file2 = dali.take_screenshot(
            resolution="1024x768",
            scenario=callback,
            scenario_args=self.driver,
            path_to_save="/tmp",
            options={
                "disable_animation": "true",
                "hide_elements": ".dg-start-banner"
            }
        )

        diff = dali.compare_images(file1, file2, "/tmp/out.png")
        self.assertEquals(0.0, diff, "The difference is %.2f%%" % diff)


if __name__ == "__main__":
    unittest.main()
