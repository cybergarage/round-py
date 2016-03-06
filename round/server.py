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
from docker import Client

class Server:
    def __init__(self):
        self.addr = ""

    def start(self):
        return False

    def stop(self):
        return False

def exec_round_process():
    if subprocess.call('/usr/local/bin/roundd') != 0:
        return False
    return True

class ProcessServer(Server):
    def __init__(self):
        Server.__init__(self)

    def start(self):
        self.process = multiprocessing.Process(target='exec_round_process')
        self.process.start()
        return True

    def stop(self):
        self.process.terminate()
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
        for keys,values in self.container.items():
            print(keys)
            print(values)

    def start(self):
        return True
        res = self.docker.start(container=self.container.get('Id'))

    def stop(self):
        return True
        return self.docker.stop(container=self.container.get('Id'))
