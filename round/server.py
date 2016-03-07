#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import socket
import subprocess
import multiprocessing

from docker import Client

from . import constants

class Server:
    def __init__(self):
        self.nodes = []

    def start(n=1):
        return False

    def stop(self):
        return False

def exec_round_process(port):
    round_addr_opt = '-i %s' % socket.gethostbyname(socket.gethostname())
    print(round_addr_opt)
    round_port_opt = '-p %d' % port
    print(round_port_opt)
    round_cmd = ['/usr/local/bin/roundd', round_addr_opt, round_port_opt]
    print(' '.join(round_cmd))
    if subprocess.call(round_cmd) != 0:
        return False
    return True

class ProcessServer(Server):
    def __init__(self):
        Server.__init__(self)
        self.processes = []

    def __del__(self):
        self.stop()

    def start(self, n=1):
        self.stop()
        print(n)
        for offset in xrange(n):
            print(offset)
            port = constants.DEFAULT_NODE_BIND_PORT + offset
            print(port)
            process = multiprocessing.Process(target=exec_round_process, args=(port,))
            process.start()
            process.join()
            print(process.exitcode)
            if process.exitcode != 0:
                self.stop()
                return False
            self.processes.append(process)
        return True

    def stop(self):
        for process in self.processes:
            process.terminate()
        self.processes = []
        return True

class ContainerServer(Server):
    def __init__(self):
        Server.__init__(self)
        #self.docker = Client(base_url='unix:///var/run/docker.sock')
        self.docker = Client(base_url='tcp://192.168.99.100:2376')
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
