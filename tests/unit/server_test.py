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
import time

from round import Server, ProcessServer, ContainerServer

def node_start_wait():
    time.sleep(0.5)

def test_server():
    srv = Server()
    assert len(srv.nodes) == 0

    assert srv.start()
    assert len(srv.nodes) == 0

    assert srv.stop()
    assert len(srv.nodes) == 0

def test_process_server():
    srv = ProcessServer()
    assert len(srv.nodes) == 0

    assert srv.start()
    assert len(srv.nodes) == 1

    node_start_wait()
    node = srv.nodes[0]
    assert node.is_alive()

    assert srv.stop()
    assert len(srv.nodes) == 0

def test_contaner_server():
    srv = ContainerServer()
    assert len(srv.nodes) == 0

    assert srv.start()
    #assert len(srv.nodes) == 1

    assert srv.stop()
    assert len(srv.nodes) == 0
