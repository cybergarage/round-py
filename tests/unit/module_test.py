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
import os

from round import Module

TEST_ECHO_MODULE_URL = 'https://raw.githubusercontent.com/cybergarage/round-py/master/tests/data/echo.json'
TEST_ECHO_MODULE_FILE = '%s/../data/%s' % (os.path.dirname(os.path.realpath(__file__)), 'echo.json')

def test_bad_module():
    module = Module()
    assert module.is_valid() == False

def test_load_echo_module():
    module = Module()
    module.load_url(TEST_ECHO_MODULE_URL)
    assert module.is_valid()

    assert module.is_url()
    assert not module.is_file()

    assert len(module.methods) == 1

    for method in module.methods:
        assert method.load_url(module.baseurl)
        assert method.is_valid()

def test_load_echo_module_file():
    module = Module()
    module.load_file(TEST_ECHO_MODULE_FILE)
    assert module.is_valid()

    assert not module.is_url()
    assert module.is_file()

    assert len(module.methods) == 1

    for method in module.methods:
        assert method.load_file(module.basepath)
        assert method.is_valid()
