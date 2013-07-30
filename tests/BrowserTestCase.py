__author__ = 'i.pavlov'

import unittest
import os
from tests.webserver import SimpleWebServer


class BrowserTestCase(unittest.TestCase):
    def setUp(self):
        # testing webserver setup
        child_directory = self.current_directory
        os.chdir(child_directory + "/src")
        self.webserver = SimpleWebServer()
        self.webserver.start()

    def tearDown(self):
        self.webserver.stop()

    def _loadPage(self, name):
        self.driver.get(self._pageURL(name))

    def _pageURL(self, name):
        return "http://localhost:%d/%s.html" % (self.webserver.port, name)