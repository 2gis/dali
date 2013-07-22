import os
import time
import json
import socket
import subprocess

from selenium.webdriver import Remote
from thrift.Thrift import TException
from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol

from bindings.py.dali import Dali as DaliThrift


def is_connectable(port):
    try:
        socket_ = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_.settimeout(1)
        socket_.connect(("localhost", port))
        socket_.close()
        return True
    except socket.error:
        return False


class Dali(object):
    def __init__(self, driver):
        """
        :type driver: Remote
        """
        try:
            ### @todo dynamic port selection
            subprocess.Popen([
                os.path.dirname(os.path.abspath(__file__)) + "/core/server/dali_server.py",
                "--port=30303"
            ])
            ### @todo add timeout
            while not is_connectable(30303):
                time.sleep(0.1)

            self.transport = TSocket.TSocket("localhost", 30303)
            self.transport = TTransport.TBufferedTransport(self.transport)
            protocol = TBinaryProtocol.TBinaryProtocol(self.transport)
            self.client = DaliThrift.Client(protocol)
            self.transport.open()
            self.client.init(driver.command_executor._url, json.dumps(driver.capabilities))
            self.transport.close()
        except TException, tx:
            ### @todo error handling
            print "%s" % tx.message

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
