__author__ = 'i.pavlov'

import unittest
import os

from dali import Dali

from selenium.webdriver import DesiredCapabilities

from tests.config import Config


class ExecutorMock(object):
    def __init__(self, url):
        self._url = url


class WebdriverMock(object):
    def __init__(self, command_executor_url, desired_capabilities):
        self.command_executor = ExecutorMock(command_executor_url)
        desired_capabilities["webdriver.remote.sessionid"] = "fake"
        self.capabilities = desired_capabilities


class ScenarioTestCase(unittest.TestCase):
    def setUp(self):
        self.current_directory = os.path.dirname(os.path.abspath(__file__))
        mock = WebdriverMock(
            command_executor_url="http://{host}:{port}/wd/hub".format(host=Config.server, port=Config.port),
            desired_capabilities=DesiredCapabilities.CHROME
        )
        self.dali = Dali(mock)

    def tearDown(self):
        pass

    def test_scenario_without_scenario_and_parameters(self):
        self.dali.run_scenario()

    def test_scenario_without_parameters(self):
        def scenario():
            pass

        self.dali.run_scenario(scenario)

    def test_scenario_with_return(self):
        def scenario():
            return 1

        result = self.dali.run_scenario(scenario)
        self.assertEqual(1, result)

    def test_scenario_with_one_parameter(self):
        def scenario(a):
            return a

        value = 1

        result = self.dali.run_scenario(scenario, value)
        self.assertEqual(scenario(value), result)

    def test_scenario_with_string_parameter(self):
        def scenario(str):
            return str.split(' ')

        string = "a b c"
        result = self.dali.run_scenario(scenario, string)
        self.assertEqual(scenario(string), result)

    def test_scenario_with_several_parameters(self):
        def scenario(a, b):
            return a + b

        result = self.dali.run_scenario(scenario, (1, 1))
        self.assertEqual(2, result)

        result = self.dali.run_scenario(scenario, [1, 1])
        self.assertEqual(2, result)

        result = self.dali.run_scenario(scenario, {'b': 1, 'a': 1})
        self.assertEqual(2, result)


if __name__ == "__main__":
    unittest.main(verbosity=2)