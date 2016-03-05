#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from docker import Client

class Server:
    def __init__(self):
        self.addr = ""

    def start():
        return False

    def stop():
        return False

class DockerServer(Server):
    def __init__(self):
        Server.__init__(self)
        #self.docker = Client(base_url='unix:///var/run/docker.sock')
        self.docker = Client(base_url='tcp://192.168.99.100:2376')
        self.container = self.docker.create_container(
            image='cybergarage/round:latest',
            command='/bin/sleep 5')
        return
        for keys,values in self.container.items():
            print(keys)
            print(values)

    def start():
        return True
        res = self.docker.start(container=self.container.get('Id'))

    def stop():
        return True
        return self.docker.stop(container=self.container.get('Id'))
