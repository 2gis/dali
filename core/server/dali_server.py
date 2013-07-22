#!/usr/bin/env python

import argparse
import socket
import sys

from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
from thrift.transport import TSocket, TTransport

from bindings.py.dali import Dali
from core.dali_core import DaliCore

parser = argparse.ArgumentParser()
parser.add_argument("--port", required=True)
port = parser.parse_args().port

handler = DaliCore()
processor = Dali.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

try:
    server.serve()
except socket.error, e:
    sys.exit(1)
