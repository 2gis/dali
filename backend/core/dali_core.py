import json
import time

from selenium.webdriver import Remote
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.remote_connection import RemoteConnection

from backend.comparison.simple import diff
from backend.supplement.scripts import Scripts


class DaliRemote(Remote):
    def __init__(self, remoteUrl, capabilities):
        ### @todo refactor me
        self.command_executor = RemoteConnection(remoteUrl)
        self.error_handler = ErrorHandler()
        self._is_remote = True
        self.start_client()
        self.session_id = capabilities["webdriver.remote.sessionid"]
        self.capabilities = capabilities


class DaliCore(object):
    def init(self, remoteUrl, capabilities):
        self.remote = DaliRemote(remoteUrl, json.loads(capabilities))
        self.resolution = "default"

    def resize(self, resolution):
        self.resolution = resolution
        w, h = tuple(resolution.split('x'))
        self.remote.set_window_size(int(w), int(h))

    def take(self, path_to_save, options):
        ### @todo implement options
        self.remote.execute_script(Scripts.disable_animation)
        ### @fixme ugly sleep
        time.sleep(1)

        filename = "%s/dali-%s-%s.png" % (path_to_save, time.time(), self.resolution)
        self.remote.get_screenshot_as_file(filename)

        return filename

    def compare(self, standard_img_path, candidate_img_path, result_img_path):
        return diff(standard_img_path, candidate_img_path, result_img_path)

    def stop(self):
        ### @todo graceful shutdown
        import sys

        sys.exit(0)
