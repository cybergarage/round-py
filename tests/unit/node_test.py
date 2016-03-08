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
import datetime

from round import ProcessServer
from round import constants

RPC_METHOD_HELLO_NAME = 'hello'

PY_ECHO_CODE = 'def %s(params):\n' \
               '  return params\n' \
               % RPC_METHOD_HELLO_NAME

def test_node_echo():
    srv = ProcessServer()
    assert srv.start()
    assert len(srv.nodes) == 1

    node = srv.nodes[0]
    assert node.is_alive()

    assert node.set_method(RPC_METHOD_HELLO_NAME, constants.SCRIPT_LANGUAGE_PYTHON, PY_ECHO_CODE)

    now = datetime.datetime.now()
    echoParam = now.strftime("%Y/%m/%d %H:%M:%S")
    print(echoParam)

    assert node.post_method(RPC_METHOD_HELLO_NAME, echoParam)
    assert node.result == echoParam

    assert srv.stop()
