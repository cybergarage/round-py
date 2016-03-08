#################################################################
#
# Round for Python
#
# Copyright (C) Satoshi Konno 2016
#
# This is licensed under BSD-style license, see file COPYING.
#
##################################################################

import json

from .. import constants

class Request:
    def __init__(self):
        self.params = {
            constants.JSON_RPC_JSONRPC: constants.JSON_RPC_VERSION,
        }

    @property
    def version(self):
        return self.params[constants.JSON_RPC_JSONRPC]

    @property
    def method(self):
        return self.params[constants.JSON_RPC_METHOD]

    @method.setter
    def method(self, method):
        self.params[constants.JSON_RPC_METHOD] = method

    @property
    def params(self):
        return self.params[constants.JSON_RPC_PARAMS]

    @params.setter
    def params(self, params):
        self.params[constants.JSON_RPC_PARAMS] = params
