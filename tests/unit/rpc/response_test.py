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

from round.rpc import Response

def test_rpc_response():
    res = Response()

    testResult = "testResult"
    res.result = testResult
    assert res.result == testResult

    testError = "testError"
    res.error = testError
    assert res.error == testError
