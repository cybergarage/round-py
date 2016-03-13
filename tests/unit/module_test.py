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

from round import Module

TEST_ECHO_MODULE = "https://raw.githubusercontent.com/cybergarage/round-py/master/tests/data/echo.json"

def test_bad_module():
    module = Module()
    assert module.is_valid() == False

def test_load_echo_module():
    module = Module()
    module.load(TEST_ECHO_MODULE)
    assert module.is_valid()
    assert len(module.methods) == 1

    for method in module.methods:
        assert method.load(module.baseurl)
        assert method.is_valid()
