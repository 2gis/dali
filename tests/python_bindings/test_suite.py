__author__ = 'i.pavlov'

import unittest

from tests.python_bindings.scenario import scenario_test
from tests.python_bindings.scenario import take_screenshot_scenario
# import sys


def suite():
    return unittest.TestSuite((
        unittest.makeSuite(scenario_test.ScenarioTestCase),
        unittest.makeSuite(take_screenshot_scenario.TakeScreenshotScenarioTestCase)
    ))


def main():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    #sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()