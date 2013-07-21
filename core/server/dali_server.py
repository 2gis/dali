#!/usr/bin/env python

import argparse
import socket

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from bindings.py.dali import Dali
from core.dali_core import DaliCore

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--port", required=True)
port = parser.parse_args().port

handler = DaliCore()
processor = Dali.Processor(handler)
### @todo pass port as a parameter
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

try:
    server.serve()
except socket.error:
    ### @todo error handling. Maybe specific exit code?
    print "Ooops"
