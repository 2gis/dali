import json
import time

from selenium.webdriver import Remote
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.remote_connection import RemoteConnection

from core.compare.pixel_diff import diff
from core.supplement.scripts import Scripts


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

    def take(self, save_path, options):
        ### @todo research and remove sleeps
        ### @todo more common options
        time.sleep(1)
        if "hide_elements" in options:
            for selector in options["hide_elements"].split(","):
                self.remote.execute_script(Scripts.hide_elements % selector)

        if "disable_animation" in options and options["disable_animation"] == "True":
            self.remote.execute_script(Scripts.disable_animation)
        time.sleep(1)

        filename = "%s/dali-%s-%s.png" % (save_path, time.time(), self.resolution)
        self.remote.get_screenshot_as_file(filename)

        return filename

    @staticmethod
    def compare(image1_path, image2_path, result_path):
        return diff(image1_path, image2_path, result_path)

    @staticmethod
    def stop():
        ### @todo graceful shutdown
        import sys

        sys.exit(0)
