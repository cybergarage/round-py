#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

from __future__ import absolute_import

import json

from .. import constants

class Request:
    def __init__(self):
        self.dict = {
            constants.JSON_RPC_JSONRPC: constants.JSON_RPC_VERSION,
        }

    def __str__(self):
        return json.dumps(self.dict)

    @property
    def version(self):
        return self.dict[constants.JSON_RPC_JSONRPC]

    @property
    def method(self):
        return self.dict[constants.JSON_RPC_METHOD]

    @method.setter
    def method(self, method):
        self.dict[constants.JSON_RPC_METHOD] = method

    @property
    def params(self):
        return self.dict[constants.JSON_RPC_PARAMS]

    @params.setter
    def params(self, params):
        self.dict[constants.JSON_RPC_PARAMS] = params
