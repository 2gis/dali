import json
import os
import socket
import subprocess
import time

from selenium.webdriver import Remote
from thrift.Thrift import TException
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from bindings.py.dali import Dali as DaliThrift
from exceptions import DaliServerConnectionError


def is_connectable(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        sock.connect(("localhost", port))
        sock.close()
        return True
    except socket.error:
        return False


def get_free_port():
    sock = socket.socket()
    sock.bind(('', 0))
    port = sock.getsockname()[1]
    sock.close()
    return port


class Dali(object):
    DALI_SERVER_PATH = os.path.dirname(os.path.abspath(__file__)) + "/core/server/dali_server.py"
    CONNECTION_TIMEOUT = 5  # in seconds

    def __init__(self, driver):
        """
        :type driver: Remote
        """
        port = get_free_port()
        subprocess.Popen([
            self.DALI_SERVER_PATH,
            "--port=%d" % port,
        ])

        t = time.time()
        while not is_connectable(port) and time.time() - t < self.CONNECTION_TIMEOUT:
            time.sleep(0.1)
        if not is_connectable(port):
            raise DaliServerConnectionError("Couldn't connect to Dali server on port %s", port)

        try:
            self.transport = TSocket.TSocket("localhost", port)
            self.transport = TTransport.TBufferedTransport(self.transport)
            protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = DaliThrift.Client(protocol)
            self.transport.open()
            self.client.init(driver.command_executor._url, json.dumps(driver.capabilities))
            self.transport.close()
        except TException, e:
            ### @todo error handling
            print "%s" % e.message

    def __del__(self):
        ### @todo graceful shutdown
        self.transport.open()
        try:
            self.client.stop()
        except TTransport.TTransportException:
            pass
        self.transport.close()

    def take_screenshot(self, resolution, scenario=None, scenario_args=None, path_to_save=None, options={}):
        ### @todo default directory for windows
        if not path_to_save:
            path_to_save = "/tmp"
        self.transport.open()
        self.client.resize(resolution)
        if callable(scenario):
            scenario(scenario_args)
        filename = self.client.take(path_to_save, options)
        self.transport.close()

        return filename

    def compare_images(self, standard, candidate, result):
        self.transport.open()
        result = self.client.compare(standard, candidate, result)
        self.transport.close()

        return result
