#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import pytest
from round import Server, ProcessServer, ContainerServer

def test_server():
    srv = Server()
    assert len(srv.nodes) == 0
    assert srv.start() != True
    assert srv.stop() != True

def test_process_server():
    srv = ProcessServer()
    assert srv.start()
    assert srv.stop()

def test_contaner_server():
    srv = ContainerServer()
    assert srv.start()
    assert srv.stop()
