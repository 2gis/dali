#!/usr/bin/env python

import socket

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from bindings.py.dali import Dali
from core.dali_core import DaliCore

handler = DaliCore()
processor = Dali.Processor(handler)
### @todo pass port as a parameter
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)

try:
    server.serve()
except socket.error:
    ### @todo error handling. Maybe specific exit code?
    print "Ooops"
