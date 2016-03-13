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

from round import Method

def test_bad_method():
    method = Method()
    assert not method.is_valid()
