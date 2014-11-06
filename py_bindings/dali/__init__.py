import json
import socket
import tempfile
import time
from threading import Thread

from common.core.dali_server import run

from selenium.webdriver import Remote
from thrift.Thrift import TException
from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from common.core.interface_implementation.dali import TDali
from common.core.interface_implementation.dali.ttypes import TOptions
from exceptions import *


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


class Options(TOptions):
    def __init__(self, *args, **kwargs):
        super(Options, self).__init__(*args, **kwargs)


class Dali(object):
    CONNECTION_TIMEOUT = 5  # in seconds

    def __init__(self, driver):
        """
        :type driver: Remote
        """
        port = get_free_port()
        self.server = Thread(target=run, args=(port,))
        self.server.daemon = True
        self.server.start()

        ### @todo add returncode managment
        if not self.server.isAlive():
            raise Exception("Server didn't start")
        else:
            pass

        t = time.time()
        while not is_connectable(port) and time.time() - t < self.CONNECTION_TIMEOUT:
            time.sleep(0.1)
        if not is_connectable(port):
            raise DaliServerConnectionError("Couldn't connect to Dali server on port %s", port)

        try:
            self.transport = TSocket.TSocket("localhost", port)
            self.transport = TTransport.TBufferedTransport(self.transport)
            protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = TDali.Client(protocol)
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
        self.server.join()

    def run_scenario(self, scenario=None, scenario_args=None):
        if callable(scenario):
            if not scenario_args:
                return scenario()
            else:
                if type(scenario_args) is dict:
                    return scenario(**scenario_args)
                elif hasattr(scenario_args, "__iter__"):
                    return scenario(*scenario_args)
                else:
                    return scenario(scenario_args)

    def take_screenshot(self, resolution, scenario=None, scenario_args=None, path_to_save=None, options=TOptions()):
        if not path_to_save:
            path_to_save = tempfile.gettempdir()
        self.transport.open()
        self.client.resize(resolution)
        self.run_scenario(scenario, scenario_args)
        filename = self.client.take(path_to_save, options)
        self.transport.close()
        return filename

    def compare_images(self, standard, candidate, result):
        self.transport.open()
        result = self.client.compare(standard, candidate, result)
        self.transport.close()
        return result
