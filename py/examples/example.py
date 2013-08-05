import unittest

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

from dali import Dali, Options


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
            driver.implicitly_wait(5)
            driver.get("http://go.2gis.com/uvaw")
            driver.find_element_by_css_selector(".dg-traf-scores-wr").click()

        dali = Dali(self.driver)
        options1 = Options(
            substitute={".dg-routs>.dg-btn-label": "Lorem Ipsum"},
            hide_elements=[".dg-start-banner"],
            disable_animation=True
        )
        options2 = Options(
            hide_elements=[".dg-start-banner"],
            disable_animation=True
        )
        file1 = dali.take_screenshot(
            resolution="1024x768",
            scenario=callback,
            scenario_args=self.driver,
            path_to_save="/tmp",
            options=options1
        )

        file2 = dali.take_screenshot(
            resolution="1024x768",
            scenario=callback,
            scenario_args=self.driver,
            path_to_save="/tmp",
            options=options2
        )

        diff = dali.compare_images(file1, file2, "/tmp/out.png")
        self.assertLessEqual(diff, 0.1, "The difference is %f" % diff)


if __name__ == "__main__":
    unittest.main()
