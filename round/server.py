#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from __future__ import absolute_import

import subprocess
import multiprocessing
import time
import socket

from docker import Client
from . import constants

LATEST_DOCKER_TAG_NAME = 'latest'

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

    def __del__(self):
        self.stop()

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
        Server.__del__(self)

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
        Server.__del__(self)

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
    def __init__(self, repository=constants.DOCKER_IMAGE_NAME, tag=LATEST_DOCKER_TAG_NAME):
        Server.__init__(self)
        docker_image = constants.DOCKER_IMAGE_NAME
        self.docker = Client(base_url='unix:///var/run/docker.sock')
        self.docker.pull(
            repository=repository,
            tag=tag,
            stream=False)
        image = '%s:%s' % (repository, tag)
        self.container = self.docker.create_container(
            image=image,
            ports=[constants.DEFAULT_NODE_BIND_PORT],
            host_config=self.docker.create_host_config(port_bindings={constants.DEFAULT_NODE_BIND_PORT:constants.DEFAULT_NODE_BIND_PORT}),
            command='/bin/sleep 1')
        print(self.container)

    def __del__(self):
        self.docker.remove_container(container=self.container.get('Id'))
        Server.__del__(self)

    def start(self, n=1):
        res = self.docker.start(container=self.container.get('Id'))
        print(res)
        return True

    def stop(self):
        res = self.docker.stop(container=self.container.get('Id'))
        print(res)
        return True
