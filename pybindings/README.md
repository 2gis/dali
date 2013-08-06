Introduction
============

Python bindings to Dali - selenium-based webpage screenshot comparison tool.

Requirements
------------

1. python-opencv to compare screenshots,
2. selenium-server-standalone to run under,
3. pip, setuptools to install.


Installing
----------

1. sudo apt-get install python-pip python-dev build-essential
2. sudo pip install --upgrade pip
3. sudo apt-get install python-opencv
4. git clone https://github.com/2gis/dali.git
5. cd dali
6. python setup.py sdist
7. sudo pip install dist/dali-*.tar.gz (for example sudo pip install dist/dali-0.1.tar.gz)

Usage
-----

### import
```python
from dali import Dali, Options
```

### dali
```python
self.driver = Remote(
    desired_capabilities=DesiredCapabilities.CHROME,
    command_executor="http://localhost:4455/wd/hub"
)
dali = Dali(self.driver)
```

### scenario
Scenario to run before taking screenshot
```python
def callback(driver):
    """
    :type driver: Remote
    """
    driver.implicitly_wait(5)
    driver.get("http://go.2gis.com/uvaw")
    driver.find_element_by_css_selector(".dg-traf-scores-wr").click()
```

### Options
| Option            | Format                                | Description                       |
| ----------------- | ------------------------------------- | --------------------------------- |
| substitute        | {"css selector": "text:, ...}         | text substitution                 |
| hide_elements     | ["css selector", "css selector", ...] | hide some content by css selector |
| disable_animation | True|False                            | disable css3 animation            |

```python
options = Options(
    substitute={".dg-routs>.dg-btn-label": "Lorem Ipsum"},
    hide_elements=[".dg-start-banner"],
    disable_animation=True
)
```

### take_screenshot
| Argument          | Type                                  |          | Description                       |
| ----------------- | ------------------------------------- |:--------:| --------------------------------- |
| resolution        | string                                |          | "800x600" etc.                    |
| scenario          | callable                              | optional | things to do before screenshot    |
| scenario_args     | (arg, ...) or [arg, ...] or arg       | optional | scenario arguments                |
| path_to_save      | string                                | optional | place to screenshot               |
| options           | Options                               | optional | options                           |

return string contains screenshot filename

```python
filename = dali.take_screenshot(
    resolution="1024x768",
    scenario=callback,
    scenario_args=self.driver,
    options=options1,
    path_to_save="./",
)
```


### compare_images
```python
diff = dali.compare_images(screenshot1, screenshot2, "./out.png")
```

example
-------

You can run this example after installation by

1. You need to start selenium-server-standalone on port 4455 (or change example.py) with binded ChromeDriver2
   You may find this link useful: https://github.com/bayandin/selenium-launchers
2. cd pybindings/examples
3. python example.py

```python
import unittest

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver import Remote

from dali import Dali, Options

class ExampleTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = Remote(
            desired_capabilities=DesiredCapabilities.CHROME,
            command_executor="http://localhost:4455/wd/hub"
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
            options=options1,
            path_to_save="./",
        )

        file2 = dali.take_screenshot(
            resolution="1024x768",
            scenario=callback,
            scenario_args=self.driver,
            options=options2,
            path_to_save="./",
        )

        diff = dali.compare_images(file1, file2, "./out.png")
        self.assertEquals(diff, 0.0, "The difference is %f" % diff)


if __name__ == "__main__":
    unittest.main()
```