import unittest
import os
import socket

from tests.webserver import SimpleWebServer
from tests.config import Config


class BrowserTestCase(unittest.TestCase):
    def setUp(self):
        # testing webserver setup
        child_directory = self.current_directory
        os.chdir(child_directory + "/src")
        self.webserver = SimpleWebServer()
        self.webserver.start()

    def tearDown(self):
        self.webserver.stop()

    def load_page(self, name):
        self.driver.get(self.page_url(name))

    def get_local_ip(self):
        # what ip can selenium server see us
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((Config.server, 0))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def page_url(self, name):
        return "http://{address}:{port}/{page}.html".format(
            address=self.get_local_ip(),
            port=self.webserver.port,
            page=name
        )