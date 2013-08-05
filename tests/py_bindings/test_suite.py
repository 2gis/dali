import unittest

from tests.py_bindings.scenario import scenario_test, take_screenshot_scenario_test
# import sys


def suite():
    return unittest.TestSuite((
        unittest.makeSuite(scenario_test.ScenarioTestCase),
        unittest.makeSuite(take_screenshot_scenario_test.TakeScreenshotScenarioTestCase)
    ))


def main():
    result = unittest.TextTestRunner(verbosity=2).run(suite())
    #sys.exit(not result.wasSuccessful())


if __name__ == "__main__":
    main()