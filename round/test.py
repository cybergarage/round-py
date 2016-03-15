#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from .server import Server, DebugServer, ProcessServer, ContainerServer
from .node import Node

class TestServer(ProcessServer):
    def __init__(self):
        ProcessServer.__init__(self)

    def __del__(self):
        self.stop()

    def start(self, n=1):
        return ProcessServer.start(self, n)

    def stop(self):
        return ProcessServer.stop(self)

class TestNode(Node):
    def __init__(self):
        Node.__init__(self)
        self.server = TestServer()
        self.server.start()
        self.start()

    def start(self):
        if not self.server.start():
            return False

        node = self.server.nodes[0]
        if not node.is_alive:
            return False

        self.set_node(node)
        return True

    def stop(self):
        self.server.stop()
        return True

    def __del__(self):
        self.stop()