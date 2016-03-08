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

from round.rpc import Request

def test_rpc_request():
    req = Request()

    testMethod = "testMethod"
    req.method = testMethod
    assert req.method == testMethod

    testParams = "testParams"
    req.params = testParams
    assert req.params == testParams
