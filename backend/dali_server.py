#!/usr/bin/env python

from thrift.transport import TSocket, TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

from thrift_py.dali import Dali
from backend.core.dali_core import DaliCore

handler = DaliCore()
processor = Dali.Processor(handler)
transport = TSocket.TServerSocket(port=30303)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
server.serve()
