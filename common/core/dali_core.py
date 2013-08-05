import json
import sys
import time

from selenium.webdriver import Remote
from selenium.webdriver.remote.errorhandler import ErrorHandler
from selenium.webdriver.remote.remote_connection import RemoteConnection

from compare.pixel_diff import diff
from supplement.scripts import Scripts


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
        ### @todo need to add some waiting mechanism, local resize is too fast
        time.sleep(1)

    def take(self, save_path, options):
        ### @todo research and remove sleeps
        ### @todo more common options
        time.sleep(1)

        for key in options.substitute.keys():
            elements = self.remote.find_elements_by_css_selector(key)
            for element in elements:
                script = "arguments[0].innerHTML='%s'" % options.substitute[key]
                self.remote.execute_script(script, element)

        for selector in options.hide_elements:
            self.remote.execute_script(Scripts.hide_elements % selector)

        if options.disable_animation:
            self.remote.execute_script(Scripts.disable_animation)

        filename = "%s/dali-%s-%s.png" % (save_path, time.time(), self.resolution)
        self.remote.get_screenshot_as_file(filename)
        return filename

    @staticmethod
    def compare(image1_path, image2_path, result_path):
        return diff(image1_path, image2_path, result_path)

    @staticmethod
    def stop():
        ### @todo graceful shutdown
        sys.exit(0)
