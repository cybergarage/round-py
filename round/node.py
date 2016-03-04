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

class Node:
    def __init__(self):
        self.port = 0
        self.address = ""
        
    def post_method(self, method, params):
        url = self.address + "+" + self.port
        r = requests.post(url, data = {"method":method})
