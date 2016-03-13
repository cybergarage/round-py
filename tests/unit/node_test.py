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

from round import TestNode
from round import constants

TEST_ECHO_MODULE = "https://raw.githubusercontent.com/cybergarage/round-py/master/tests/data/echo.json"

TEST_RPC_METHOD_HELLO_NAME = 'hello'
TEST_PY_ECHO_CODE = 'def %s(params):\n' \
                    '  return params\n' \
                    % TEST_RPC_METHOD_HELLO_NAME

def test_node_echo():

    node = TestNode()
    assert node.is_alive

    assert node.set_method(TEST_RPC_METHOD_HELLO_NAME, constants.SCRIPT_LANGUAGE_PYTHON, TEST_PY_ECHO_CODE)

    now = datetime.datetime.now()
    echoParam = now.strftime("%Y/%m/%d %H:%M:%S")

    assert node.post_method(TEST_RPC_METHOD_HELLO_NAME, echoParam)
    assert node.result == echoParam

def test_node_load_echo_module():

    node = TestNode()
    assert node.is_alive

    assert node.load_module(TEST_ECHO_MODULE)

    now = datetime.datetime.now()
    echoParam = now.strftime("%Y/%m/%d %H:%M:%S")

    assert node.post_method(TEST_RPC_METHOD_HELLO_NAME, echoParam)
    assert node.result == echoParam
