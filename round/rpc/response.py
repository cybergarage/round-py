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

class Response:
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
    def result(self):
        return self.dict[constants.JSON_RPC_RESULT]

    @result.setter
    def result(self, result):
        self.dict[constants.JSON_RPC_METHOD] = result

    @property
    def error(self):
        return self.dict[constants.JSON_RPC_ERROR]

    @error.setter
    def error(self, error):
        self.dict[constants.JSON_RPC_ERROR] = error
