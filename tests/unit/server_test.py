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
from round import Server, DockerServer

def test_server():
    srv = Server()

def test_contaner_server():
    srv = DockerServer()
    assert srv.start
    assert srv.stop
