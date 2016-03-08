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
import requests

from . import constants
from .rpc.request import Request

class Node:
    def __init__(self):
        self.port = 0
        self.address = ""
        self.rpcRes = {}

    @property
    def result(self):
        return self.rpcRes[constants.JSON_RPC_RESULT]

    @property
    def error(self):
        return self.rpcRes[constants.JSON_RPC_ERROR]

    def create_http_url(self, path):
        url = 'http://%s:%d%s' % (self.address, self.port, path)
        return url

    def is_alive(self):
        rootURL = self.create_http_url("/")
        res = requests.get(rootURL)
        if res.status_code != 200:
            return False
        return True

    def post_method(self, method, params):
        rpcURL = self.create_http_url(constants.RPC_HTTP_ENDPOINT)

        # TODO : Couldn't Request .. Why?
        rpcReq = Request()
        rpcReq.method = method
        rpcReq.params = params

        # FIXME : Use Request class
        reqParams = {
            constants.JSON_RPC_JSONRPC: constants.JSON_RPC_VERSION,
            constants.JSON_RPC_METHOD: method,
            constants.JSON_RPC_PARAMS: params,
        }
        reqContent = json.dumps(reqParams)

        res = requests.post(rpcURL,
                            #data=str(rpcReq),
                            data=reqContent,
                            headers={'Content-Type': constants.RPC_HTTP_CONTENT_TYPE})

        try:
            self.rpcRes = res.json()
        except ValueError:
            self.rpcRes = {}

        if res.status_code != 200:
            return False

        return True

    def set_method(self, name, lang, code):
        params = {
            constants.SYSTEM_METHOD_PARAM_NAME: name,
            constants.SYSTEM_METHOD_PARAM_LANGUAGE: lang,
            constants.SYSTEM_METHOD_PARAM_CODE: code,
        }
        return self.post_method(method=constants.SYSTEM_METHOD_SET_METHOD, params=params)
