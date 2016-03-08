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

class Response:
    def __init__(self):
        self.params = {
            constants.JSON_RPC_JSONRPC: constants.JSON_RPC_VERSION,
        }

    @property
    def version(self):
        return self.params[constants.JSON_RPC_JSONRPC]

    @property
    def result(self):
        return self.params[constants.JSON_RPC_RESULT]

    @result.setter
    def result(self, result):
        self.params[constants.JSON_RPC_METHOD] = result

    @property
    def error(self):
        return self.params[constants.JSON_RPC_ERROR]

    @error.setter
    def error(self, error):
        self.params[constants.JSON_RPC_ERROR] = error
