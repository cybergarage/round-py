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

class Node:
    def __init__(self):
        self.port = 0
        self.address = ""

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
        rpcURL = self.create_http_url(round.constants.RPC_HTTP_ENDPOINT)
        res = requests.post(rpcURL,
                            data = {"method":method},
                            headers={'Content-Type': round.constants.RPC_HTTP_CONTENT_TYPE})

