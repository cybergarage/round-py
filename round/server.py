#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import subprocess
import multiprocessing
import time
import socket

from docker import Client

DOCKER_IF_ADDR = '192.168.99.1'

from . import constants
from .node import Node

def node_process_wait():
    time.sleep(0.5)

def node_get_hostaddr():
    hosts = socket.gethostbyname_ex(socket.gethostname())
    ifaddrs = hosts[2]
    if isinstance(ifaddrs, str):
        return ifaddrs
    for ifaddr in ifaddrs:
        if ifaddr == DOCKER_IF_ADDR:
            continue
        return ifaddr
    return socket.gethostbyname(socket.gethostname())

class Server:
    def __init__(self):
        self.nodes = []

    def start(n=1):
        return True

    def stop(self):
        self.nodes = []
        return True

def exec_round_process(addr, port):
    # Run as standalone mode
    round_addr_opt = '-i %s' % addr
    round_port_opt = '-p %d' % port
    round_cmd = ['/usr/local/bin/roundd', '-f', round_addr_opt, round_port_opt]
    if subprocess.call(round_cmd) != 0:
        return False
    return True

class DebugServer(Server):
    def __init__(self):
        Server.__init__(self)

    def __del__(self):
        self.stop()

    def start(self, n=1):
        node = Node()
        node.address = node_get_hostaddr()
        node.port = constants.DEFAULT_NODE_BIND_PORT
        self.nodes.append(node)
        return Server.start(self)

    def stop(self):
        return Server.stop(self)

class ProcessServer(Server):
    def __init__(self):
        Server.__init__(self)
        self.processes = []

    def __del__(self):
        self.stop()

    def start(self, n=1):
        self.stop()
        for offset in xrange(n):
            addr = node_get_hostaddr()
            port = constants.DEFAULT_NODE_BIND_PORT + offset
            process = multiprocessing.Process(target=exec_round_process, args=(addr, port))
            process.start()

            # Run as standalone mode
            #process.join()
            #print(process.exitcode)
            #if process.exitcode != 0:
            #    self.stop()
            #    return False

            node_process_wait()

            self.processes.append(process)

            node = Node()
            node.address = addr
            node.port = port
            self.nodes.append(node)
        return Server.start(self)

    def stop(self):
        for process in self.processes:
            process.terminate()
            node_process_wait()
        self.processes = []
        return Server.stop(self)

class ContainerServer(Server):
    def __init__(self):
        Server.__init__(self)
        #self.docker = Client(base_url='unix:///var/run/docker.sock')
        #self.docker = Client(base_url='tcp://192.168.99.100:2376')
        return
        self.container = self.docker.create_container(
            image='cybergarage/round:latest',
            command='/bin/sleep 5')
        #for keys,values in self.container.items():
        #    print(keys)
        #    print(values)

    def start(self, n=1):
        return True
        res = self.docker.start(container=self.container.get('Id'))

    def stop(self):
        return True
        return self.docker.stop(container=self.container.get('Id'))
